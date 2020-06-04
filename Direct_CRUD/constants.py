driver_path = 'chromedriver.exe'
g_link = "https://accounts.google.com"
identifier_element = "identifier"
gmail_id = "pranjal@doctormm.com"
xpath_next = '//*[@id="identifierNext"]/span/span'
pass_element = "password"
gmail_pass = "6P4M%X2[:jVsf9)f1352@7323451"
xpath_login = '//*[@id="passwordNext"]/span/span'
ss_url = "https://docs.google.com/spreadsheets/d/17pUrPnz7D-6pjqZkpG6VmlBhj2RBC3KsSP65dXON9hk/edit#gid=0"

ss_api = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
json_cred_path = 'survey_cred.json'

ss_name = 'NewSurvey_template_based1'
s_name = 'Template1'
data2insert = ["pain1", "progress", "Since your pain began HOW HAS IT CHANGED?", "", "radio", "yes", "improved, worsened, stayed the same"]
insert_row = 4

delete_row = 4

update_row_number = 1
update_col_number = 1
update_value = "section"


xpath_ss_tools = '//*[@id="docs-tools-menu"]'
xpath_ss_tools_script_editor = '//*[@id=":gq"]/div/span'
xpath_gs_publish = '//*[@id="macros-publish-menu"]'
xpath_gs_deploy = '//*[@id=":1m"]'
xpath_gs_web_new = '//*[@value="New"]'
xpath_gs_update = '//*[@class="gwt-Button action submit"]' 
xpath_gs_latest_c = '//*[@id="dev-mode"]'