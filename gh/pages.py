from github import gh, User # Organization


def writeUserPage(username):
  udata = User(username)
  name = f"({udata.getName()})" if udata.getName() else ""

  with open("./templates/upage.html", "w+") as f:
    f.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitHub Profile: {udata.getUsername()} {name}</title>
</head>
<body style="background:black;background-image:url('https://cdn.wallpapersafari.com/15/28/pqWJsO.jpg');">
  <font color="#FFFFFF" size="+3">GitHub Profile for: </font><font color="#0000FF" size="+3"><b>{udata.getUsername()} {name}</b></font>
  <div style="background-color:black; width:400px; border:3px solid orange; border-radius:3px;">
    <figure>
      <img src="{udata.getAvatar()}" style="width:100px;height=100px;" usemap="#rect" id="hello">
    </figure>
      <font size="+1" color="#0AD0E8">{udata.getBio() if udata.getBio() else "No biography"}</font><br>
      <br>
      <font size="+1" color="#FFFFFF"><b>Created at: </b></font><font size="+1" color="#0AD0E8">{gh.getDate(udata.getCreated())}</font><br>
      <font size="+1" color="#FFFFFF"><b>Last updated at: </b></font><font size="+1" color="#0AD0E8">{gh.getDate(udata.getLastUpdated())}</font><br>
      <font size="+1" color="#FFFFFF"><b>Location: </b></font> <font size="+1" color="#0AD0E8">{udata.getLocation() if udata.getLocation() else None}</font><br>
      <font size="+1" color="#FFFFFF"><b>Company: </b></font><font size="+1" color="#0AD0E8">{udata.getCompany() if udata.getCompany() else None}</font><br>
      <font size="+1" color="#FFFFFF"><b>Website: </b></font><font size="+1" color="#0AD0E8">{udata.getWebsite() if udata.getWebsite() else None}</font><br>
      <br>
      <font size="+1" color="#FFFFFF"><b>Repository count: </b></font><font size="+1" color="#0AD0E8">{udata.getRepoCount() if udata.getRepoCount() else None}</font><br>
      <font size="+1" color="#FFFFFF"><b>Gist count: </b></font><font size="+1" color="#0AD0E8">{udata.getGistCount() if udata.getGistCount() else None}</font><br>
      <br>
      <font size="+1" color="#FFFFFF"><b>Follower count: </b></font><font size="+1" color="#0AD0E8">{udata.getFollowerCount() if udata.getFollowerCount() else "No followers. Boo - hoo..."}</font><br>
      <font size="+1" color="#FFFFFF"><b>Following count: </b></font><font size="+1" color="#0AD0E8">{udata.getFollowingCount() if udata.getFollowingCount() else "Not following anyone... got any friends u might wanna drop a follow?"}</font><br>
      <br>
      <font size="+1" color="#FFFFFF"><b>Starred Count: </b></font><font size="+1" color="#0AD0E8">{udata.getStarredCount() if udata.getStarredCount() else "Nothing starred. Hmmmmm... u might wanna check out some of the cool stuff that's out there."}</font><br>
      <font size="+1" color="#FFFFFF"><b>Organization count: </b></font><font size="+1" color="#0AD0E8">{udata.getOrgCount() if udata.getOrgCount() else None}</font><br>
      <font size="+1" color="#FFFFFF"><b>Administrator? </b></font><font size="+1" color="#0AD0E8">{"Yep, don't do anything wrong in front of this one." if udata.isAdmin() else "Nope, not an admin."}</font>
  </div><br>
</body>
</html>
            ''')