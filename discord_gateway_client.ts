import { WebSocketClient, StandardWebSocketClient } from "https://deno.land/x/websocket@v0.1.3/mod.ts"
import Client from "../client/client.ts";
import { READY, MESSAGE_CREATE } from "./handlers.ts";

/*
A Discord Gateway client written in TypeScript. This is a part of my Discord API/Gateway Wrapper.
*/

export default class WebSocketManager {
    private ws!: WebSocketClient;
    private client!: Client;

    constructor(client: Client) {
        this.ws = new StandardWebSocketClient("wss://gateway.discord.gg/?v=6&encoding=json");
        this.client = client;
    }

    async handle_response(resp: any, token: string) {
        const {op, d, t} = JSON.parse(resp);

            switch(op) {
                case 10:
                    await this.heartbeat(d.heartbeat_interval);
                    await this.identify(token);
                    break;
                case 9:
                    throw "Invalid gateway session.";
                case 0:
                    switch(t) {
                        case "READY":
                            READY(this.client, d);
                            break;
                        case "MESSAGE_CREATE":
                            MESSAGE_CREATE(this.client, d);
                            break;
                    }
                    break;
                default:
                    break;
            }
    }

    async connect(token: string) {
        this.ws.on("message", async (message) => {
            await this.handle_response(message.data, token);
        });
    }

    async heartbeat(interval: number) {
        const payload = {
            op: 1,
            d: null
        }
        
        setInterval(() => {
            this.ws.send(JSON.stringify(payload));
        }, interval);
    }

    async identify(token: string) {
        const payload = {
            op: 2,
            d: {
                token: token,
                properties: {
                    $os: Deno.build.os,
                    $browser: "discord-lib",
                    $device: "discord-lib"
                }
            }
        }
        this.ws.send(JSON.stringify(payload));
    }
}
