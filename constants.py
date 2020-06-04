driverPath = 'chromedriver.exe'
gLink = "https://accounts.google.com"
identifierElement = "identifier"
gmailId = "pranjal@doctormm.com"
xpathNext = '//*[@id="identifierNext"]/span/span'
passElement = "password"
gmailPass = "6P4M%X2[:jVsf9)f1352@7323451"
xpathLogin = '//*[@id="passwordNext"]/span/span'
ssUrl = "https://docs.google.com/spreadsheets/d/17pUrPnz7D-6pjqZkpG6VmlBhj2RBC3KsSP65dXON9hk/edit#gid=0"

ssApi = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
json = 'survey_cred.json'

ssName = 'NewSurvey_template_based1'
sName = 'Template1'
data2Insert = ["pain", "pranjal", "Since your pain began HOW HAS IT CHANGED?", "", "radio", "yes", "improved, worsened, stayed the same"]
insertIndex = 4

deleteRow = 4

updateRowNumber = 1
updateColNumber = 2
updateValue = "code"

xpathSsTools =  '//*[@id="docs-tools-menu"]'
xpathSsToolsScriptEditor = '//*[contains(@aria-label, "Script editor e")]'
xpathGsPublish = '//*[@id="macros-publish-menu"]'
xpathGsDeploy = '/html/body/div[13]/div[1]'
xpathGsWebNew = '//*[@value="New"]'
xpathGsUpdate = '//*[@class="gwt-Button action submit"]' 
xpathGsLatestC = '//*[@id="dev-mode"]'