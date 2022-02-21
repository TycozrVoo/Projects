let data = document.getElementById("user");
document.getElementById("submit").addEventListener("click", function() {
  window.location.href = "https://gh.firestardev.repl.co/user_query?user=" + data.value;
});