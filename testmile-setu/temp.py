from setu.core.config.processor import *

root_dir = "/Users/rahulverma/Documents/github_tm/daksha/daksha-examples/"
p = "/Users/rahulverma/Documents/github_tm/setu/testmile-setu/setu/core/config/"
cprocessor = ProjectConfigProcessor()
config = cprocessor.process_project_conf(root_dir)
print(config.setu_config.value(SetuConfigOption.BROWSER_NAME))
print(config.user_config.value("HELLO_THERE"))