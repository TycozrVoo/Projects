import requests


class gh:

  def __init__(self):
    self.base_api_url = "https://api.github.com"
    
  def request(self, endpoint):
    r = requests.get(self.base_api_url + endpoint)
    return r

  def get_data_len(self, endpoint):
    return len(self.request(endpoint).json())

  def isInvalid(self, name, *isOrg):
    if isOrg:
      r = requests.head(f"{self.base_api_url}/orgs/{name}")
      if r.status_code >= 400:
        return True

    r = requests.head(f"{self.base_api_url}/users/{name}")
    if r.status_code >= 400:
      return True

  @classmethod
  def getDate(cls, s):
    day = s.split("T")[0]

    return day

class User(gh):
  
  def __init__(self, username):
    super().__init__()
    self.data = self.request(f"/users/{username}").json()
    
    self.username = None # self.data["username"]
    self.name = None # self.data["name"]
    self.repo_count = None # self.data["public_repos"]
    self.gist_count = None # self.data["public_gists"]
    self.bio = None # self.data["bio"]
    self.last_updated = None # self.data["updated_at"]
    self.created_at = None # self.data["created_at"]
    self.avatar = None # self.data["avatar_url"]
    self.follower_count = None # self.data["followers"]
    self.following_count = None # self.data["following"]
    self.starred_count = None # self.get_data_len(f"/users/{username}/starred")
    self.organization_count = None # self.get_data_len(f"/users/{username}/orgs")
    self.is_github_admin = None # self.data["site_admin"]
    self.company = None # self.data["company"]
    self.website = None # self.data["blog"]
    self.location = None # self.data["location"]

  def getUsername(self):
    if not self.username:
      self.username = self.data["login"]
      return self.username
    else:
      return self.username

  def getName(self):
    if not self.name:
      self.name = self.data["name"]
      return self.name
    else:
      return self.name

  def getRepoCount(self):
    if not self.repo_count:
      self.repo_count = self.data["public_repos"]
      return self.repo_count
    else:
      return self.repo_count

  def getGistCount(self):
    if not self.gist_count:
      self.gist_count = self.data["public_gists"]
      return self.gist_count
    else:
      return self.gist_count

  def getBio(self):
    if not self.bio:
      self.bio = self.data["bio"]
      return self.bio
    else:
      return self.bio

  def getLastUpdated(self):
    if not self.last_updated:
      self.last_updated = self.data["updated_at"]
      return self.last_updated
    else:
      return self.last_updated

  def getCreated(self):
    if not self.created_at:
      self.created_at = self.data["created_at"]
      return self.created_at
    else:
      return self.created_at

  def getAvatar(self):
    if not self.avatar:
      self.avatar = self.data["avatar_url"]
      return self.avatar
    else:
      return self.avatar

  def getFollowerCount(self):
    if not self.follower_count:
      self.follower_count = self.data["followers"]
      return self.follower_count
    else:
      return self.follower_count

  def getFollowingCount(self):
    if not self.following_count:
      self.following_count = self.data["following"]
      return self.following_count
    else:
      return self.following_count

  def getStarredCount(self):
    if not self.starred_count:
      self.starred_count = self.get_data_len(f"/users/{self.getUsername()}/starred")
      return self.starred_count
    else:
      return self.starred_count

  def getOrgCount(self):
    if not self.organization_count:
      self.organization_count = self.get_data_len(f"/users/{self.getUsername()}/orgs")
      return self.organization_count
    else:
      return self.organization_count

  def isAdmin(self):
    if not self.is_github_admin:
      self.is_github_admin = self.data["site_admin"]
      return self.is_github_admin
    else:
      return self.is_github_admin

  def getCompany(self):
    if not self.company:
      self.company = self.data["company"]
      return self.company
    else:
      return self.company

  def getWebsite(self):
    if not self.website:
      self.website = self.data["blog"]
      return self.website
    else:
      return self.website

  def getLocation(self):
    if not self.location:
      self.location = self.data["location"]
      return self.location
    else:
      return self.location

class Organization(gh):

  def __init__(self, org_name):
    self.data = self.request(f"orgs/{org_name}").json()