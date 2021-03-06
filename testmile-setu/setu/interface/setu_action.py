from enum import Enum, auto

class SetuActionType(Enum):
    TESTSESSION_INIT = auto()
    TESTSESSION_FINISH = auto()

    TESTSESSION_REGISTER_CONFIG = auto()

    TESTSESSION_CREATE_FILE_DATA_SOURCE = auto()

    TESTSESSION_LAUNCH_GUIAUTOMATOR = auto()
    TESTSESSION_QUIT_GUIAUTOMATOR = auto()

    TESTSESSION_CREATE_GUI = auto()

    CONFIGURATOR_GET_SETU_OPTION_VALUE = auto()
    CONFIGURATOR_GET_USER_OPTION_VALUE = auto()

    DATASOURCE_GET_NEXT_RECORD = auto()
    DATASOURCE_GET_ALL_RECORDS = auto()
    DATASOURCE_RESET = auto()

    GUIAUTO_BROWSER_GO_TO_URL = auto()
    GUIAUTO_BROWSER_GO_BACK = auto()
    GUIAUTO_BROWSER_GO_FORWARD = auto()
    GUIAUTO_BROWSER_REFRESH = auto()
    GUIAUTO_BROWSER_EXECUTE_JAVASCRIPT = auto()

    GUIAUTO_CREATE_ELEMENT = auto()
    GUIAUTO_CREATE_MULTIELEMENT = auto()
    GUIAUTO_CREATE_DROPDOWN = auto()
    GUIAUTO_CREATE_RADIOGROUP = auto()
    GUIAUTO_CREATE_FRAME = auto()
    GUIAUTO_CREATE_ALERT = auto()

    GUIAUTO_GET_MAIN_WINDOW = auto()
    GUIAUTO_SET_SLOMO = auto()

    GUIAUTO_WEB_ALERT_CONFIRM = auto()
    GUIAUTO_WEB_ALERT_DISMISS = auto()
    GUIAUTO_WEB_ALERT_GET_TEXT = auto()
    GUIAUTO_WEB_ALERT_SEND_TEXT = auto()

    GUIAUTO_GUI_CREATE_GUI = auto()

    GUIAUTO_ELEMENT_ENTER_TEXT = auto()
    GUIAUTO_ELEMENT_SET_TEXT = auto()
    GUIAUTO_ELEMENT_CLEAR_TEXT = auto()

    GUIAUTO_ELEMENT_CLICK = auto()

    GUIAUTO_ELEMENT_WAIT_UNTIL_CLICKABLE = auto()

    GUIAUTO_ELEMENT_CHECK = auto()
    GUIAUTO_ELEMENT_UNCHECK = auto()

    GUIAUTO_DROPDOWN_HAS_VALUE_SELECTED = auto()
    GUIAUTO_DROPDOWN_HAS_INDEX_SELECTED = auto()
    GUIAUTO_DROPDOWN_SELECT_BY_VALUE = auto()
    GUIAUTO_DROPDOWN_SELECT_BY_INDEX = auto()
    GUIAUTO_DROPDOWN_GET_FIRST_SELECTED_OPTION_VALUE  = auto()        
    GUIAUTO_DROPDOWN_HAS_VISIBLE_TEXT_SELECTED = auto()
    GUIAUTO_DROPDOWN_GET_FIRST_SELECTED_OPTION_TEXT = auto()
    GUIAUTO_DROPDOWN_SELECT_BY_VISIBLE_TEXT = auto()

    GUIAUTO_RADIOGROUP_HAS_VALUE_SELECTED = auto()
    GUIAUTO_RADIOGROUP_HAS_INDEX_SELECTED = auto()
    GUIAUTO_RADIOGROUP_SELECT_BY_VALUE = auto()
    GUIAUTO_RADIOGROUP_SELECT_BY_INDEX = auto()
    GUIAUTO_RADIOGROUP_GET_FIRST_SELECTED_OPTION_VALUE  = auto()

    GUIAUTO_DOMROOT_FOCUS = auto()
    GUIAUTO_DOMROOT_CREATE_FRAME = auto()

    GUIAUTO_FRAME_FOCUS = auto()
    GUIAUTO_FRAME_CREATE_FRAME = auto()
    GUIAUTO_FRAME_GET_PARENT = auto()

    GUIAUTO_WINDOW_FOCUS = auto()
    GUIAUTO_WINDOW_GET_TITLE = auto()

    GUIAUTO_MAIN_WINDOW_MAXIMIZE = auto()
    GUIAUTO_MAIN_WINDOW_CREATE_CHILD_WINDOW = auto()
    GUIAUTO_MAIN_WINDOW_GET_LATEST_CHILD_WINDOW = auto()
    GUIAUTO_MAIN_WINDOW_CLOSE_ALL_CHILD_WINDOWS = auto()

    GUIAUTO_CHILD_WINDOW_CLOSE = auto()