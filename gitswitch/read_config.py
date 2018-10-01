import configparser

config = configparser.ConfigParser()
config_file = ".gitswitchrc"

def get_property(profile, prop):
  
  config.read(config_file)
  if profile in config:
    if prop in config[profile]:
      return config[profile]['user']
    else:
      print "property {} does not exists in profile {}".format(prop, profile)
      return None
  else:
    print "profile {} does not exist in config".format(profile)

print get_property('personal','user')

  
  
