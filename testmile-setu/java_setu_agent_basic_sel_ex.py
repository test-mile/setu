from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.guiauto.config import ex

automator = GuiAutomator("http://localhost:9898", ex)
automator.launch()
automator.go_to("https://www.google.com?q=Setu")
automator.quit()