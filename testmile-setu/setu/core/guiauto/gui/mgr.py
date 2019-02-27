import re
import os
from enum import Enum, auto
from collections import namedtuple

from setu.core.config.config_types import SetuConfigOption

class GuiManager:
    
    PAGE_MAP = {}

    @classmethod
    def create_gui(self):
        pass

class GuiAutomationContext(Enum):
    pass

class FileFormat(Enum):
    GNS = auto()
    XLS = auto()
    XLSX = auto()

class MobileNativeLocateWith(Enum):
    ID = auto()
    NAME = auto() 
    XPATH = auto() 
    CLASS = auto() 
    LINK_TEXT = auto() 
    PARTIAL_LINK_TEXT = auto() 
    TAG = auto()
    X_TEXT = auto() 
    X_TITLE = auto() 
    X_PARTIAL_TEXT = auto() 
    X_TYPE = auto() 
    X_VALUE = auto() 
    X_IMAGE_SRC = auto()

class MobileWebLocateWith(Enum):
    ID = auto()
    NAME = auto() 
    XPATH = auto() 
    CSS = auto()
    CLASS = auto() 
    LINK_TEXT = auto() 
    PARTIAL_LINK_TEXT = auto() 
    TAG = auto()
    X_TEXT = auto() 
    X_TITLE = auto() 
    X_PARTIAL_TEXT = auto() 
    X_TYPE = auto() 
    X_VALUE = auto() 
    X_IMAGE_SRC = auto()

class NativeLocateWith(Enum):
    ID = auto()
    NAME = auto() 
    XPATH = auto() 
    CLASS = auto() 
    LINK_TEXT = auto() 
    PARTIAL_LINK_TEXT = auto() 
    X_TEXT = auto() 
    X_TITLE = auto() 
    X_PARTIAL_TEXT = auto() 
    X_TYPE = auto() 
    X_VALUE = auto() 
    X_IMAGE_SRC = auto()

class VisualLocateWith(Enum):
    IMAGE = auto()

class WebLocateWith(Enum):
    ID = auto()
    NAME = auto() 
    XPATH = auto() 
    CSS = auto()
    CLASS = auto() 
    LINK_TEXT = auto() 
    PARTIAL_LINK_TEXT = auto() 
    TAG = auto()
    X_TEXT = auto() 
    X_TITLE = auto() 
    X_PARTIAL_TEXT = auto() 
    X_TYPE = auto() 
    X_VALUE = auto() 
    X_IMAGE_SRC = auto()

class GenericLocateWith(Enum):
    ID = auto()
    NAME = auto() 
    XPATH = auto() 
    CSS = auto()
    CLASS = auto() 
    LINK_TEXT = auto() 
    PARTIAL_LINK_TEXT = auto() 
    TAG = auto()
    X_TEXT = auto() 
    X_TITLE = auto() 
    X_PARTIAL_TEXT = auto() 
    X_TYPE = auto() 
    X_VALUE = auto() 
    X_IMAGE_SRC = auto()
    IMAGE = auto()

Locator = namedtuple("Locator", ("ltype", "lvalue"))
GuiGenericLocator = namedtuple("GuiGenericLocator", ("ltype", "lvalue"))

class GuiElementType(Enum):
    TEXTBOX = auto()
    PASSWORD = auto()
    LINK = auto()
    BUTTON = auto()
    SUBMIT_BUTTON = auto()
    DROPDOWN = auto()
    CHECKBOX = auto()
    RADIO = auto()
    IMAGE = auto()

class GuiElementMetaData:
    BASIC_LOCATORS = {
        GenericLocateWith.ID,
        GenericLocateWith.NAME,
        GenericLocateWith.CLASS,
        GenericLocateWith.LINK_TEXT,
        GenericLocateWith.PARTIAL_LINK_TEXT,
        GenericLocateWith.XPATH,
        GenericLocateWith.CSS,
        GenericLocateWith.TAG,
        GenericLocateWith.IMAGE
    }

    XTYPE_LOCATORS = {
        GuiElementType.TEXTBOX: "//input[@type='text']",
        GuiElementType.PASSWORD: "//input[@type='password']",
        GuiElementType.LINK: "//a",
        GuiElementType.BUTTON: "//input[@type='button']",
        GuiElementType.SUBMIT_BUTTON: "//input[@type='submit']",
        GuiElementType.DROPDOWN: "//select",
        GuiElementType.CHECKBOX: "//input[@type='checkbox']",
        GuiElementType.RADIO: "//input[@type='radio']",
        GuiElementType.IMAGE: "//img",
    }

    XPATH_LOCATORS = {
        GenericLocateWith.X_TEXT : "//*[text()='{}}']",
        GenericLocateWith.X_PARTIAL_TEXT : "//*[contains(text(),'{}')]",
        GenericLocateWith.X_VALUE : "//*[@value='{}']",
        GenericLocateWith.X_TITLE : "//*[@title='{}']",
        GenericLocateWith.X_IMAGE_SRC : "//img[@src='{}']"
    }

    def __init__(self, raw_locators):
        self.__raw_locators = raw_locators
        self.__locators = []
        self.__process()

    @property
    def locators(self):
        return self.__locators

    def __process(self):
        for raw_locator in self.__raw_locators:
            rltype = raw_locator.ltype
            rlvalue = raw_locator.lvalue
            try:
                generic_locate_with = GenericLocateWith[rltype.upper()]
            except:
                raise Exception("Invalid locator across all automators: {}".format(rltype))
            else:
                if generic_locate_with in self.BASIC_LOCATORS:
                    self.__add_locator(generic_locate_with, rlvalue)
                elif generic_locate_with in self.XPATH_LOCATORS:
                    self.__add_locator(GenericLocateWith.XPATH, self.XPATH_LOCATORS[generic_locate_with].format(rlvalue))
                elif generic_locate_with == GenericLocateWith.X_TYPE:
                    try:
                        elem_type = GuiElementType[rlvalue.upper()]
                    except:
                        raise Exception("Unsupported element type for XTYPE locator: " + rlvalue)
                    else:
                        self.__add_locator(GenericLocateWith.XPATH, self.XTYPE_LOCATORS[elem_type])
                else:
                    raise Exception("Locator not supported yet by Setu: " + rltype)

    def __add_locator(self, locator_type, locator_value):
        self.locators.append(GuiGenericLocator(locator_type, locator_value))

class GuiNamespace:

    def __init__(self):
        super().__init__()
        # dict <string, dict<GuiAutomationContext, GuiElementMetaData>>
        self.__ns = {}

    def add_element_meta_data(self, name, context, raw_locators):
        emd = GuiElementMetaData(raw_locators)
        name = name.lower()
        if not self.has(name):
            self.__ns[name] = {}
        self.__ns[name][context] = emd

    def has(self, name):
        return name.lower() in self.__ns

    def has_context(self, name, context):
        if self.has(name):
            return context in self.__ns[name.lower()]
        return False

    # Needs to be thread-safe
    # Returns emd for a context for a given gui name
    def get_meta_data(self, name, context):
        if not self.has(name):
            raise Exception("Gui namespace does not contain element with name: {}".format(name))
        elif not self.has_context(name, context):
            raise Exception("Gui namespace does not contain element with name: {} for context {}".format(name, context))
        
        return self.__ns[name.lower()][context]

class BaseGuiNamespaceLoader:

    def __init__(self, name):
        self.__name = name
        self.__namespace = GuiNamespace()

    @property
    def name(self):
        return self.__name

    @property
    def namespace(self):
        return self.__namespace

    # Needs to be thread safe
    def add_element_meta_data(self, name, context, locators):
        self.__namespace.add_element_meta_data(name, context, locators)

    def _raise_notafile_exception(self, file_path):
        raise Exception("{} is not a file.".format(file_path))

    def _raise_filenotfound_exception(self, file_path):
        raise Exception("{} is not a valid file path.".format(file_path))

    def _raise_relativepath_exception(self, file_path):
        raise Exception("Gui namespace loader does not accept relative file path. {} is not a full file path.".format(file_path))


class GuiNameStore:

    def __init__(self, name):
        # dict<String, GuiNameStore>
        self.__ns_map = {}

    # Needs to be thread safe
    def has_namespace(self, name):
        return name in self.__ns_map

    # loader is GuiNamespaceLoader
    # Needs to be thread safe
    def load_namespace(self, name, loader):
        if not self.has_namespace(name):
            loader.load()
            self.__ns_map[name.lower()] = loader.namespace

        return self.__ns_map[name.lower()]

    # Needs to be thread-safe
    def get_namespace(self, name):
        return self.__ns_map[name.lower()]

class NamespaceFileLoader(BaseGuiNamespaceLoader):

    def __init__(self, ns_file_path):
        super().__init__("Default Gui Namespace File Loader")
        self.__ns_file = None
        self.__ns_path = None
        self.name_pattern = re.compile(r"\[\s*(.*?)\s*\]")
        self.platform_pattern = re.compile(r"\s*#\s*(.*?)\s*")
        self.locator_pattern = re.compile(r"\s*(.*?)\s*=\s*(.*?)\s*")
        self.header_found = False
        self.last_header = None
        self.last_auto_contexts = None # list of auto contexts
        #Map<String, Map<GuiAutomationContext,List<Locator>>>
        self.__ns = {}

        if not os.path.isabs(ns_file_path):
            super()._raise_relativepath_exception(ns_file_path)
        elif not os.path.exists(ns_file_path):
            super()._raise_filenotfound_exception(ns_file_path)
        elif not os.path.isfile(ns_file_path):
            super()._raise_notafile_exception(ns_file_path)

        self.__ns_path = ns_file_path
        self.__ns_file = open(self.__ns_path)

    def __match_header(self, input):
        match = self.name_pattern.match(input)
        if match:
            current_header = match.group(1)
            if not self.last_header:
                last_header = current_header
            elif last_header.lower() == current_header.lower():
                raise Exception("Found duplicate namespace definition for {} element.".format(last_header))
            else:
                if len(self.__ns[last_header]) == 0:
                    raise Exception("Found empty namespace definition for {} element.".format(last_header))
                else:
                    for context, data in self.__ns[last_header].items():
                        if len(data) == 0:
                            raise Exception("Found empty namespace definition for {} context for {} element.".format(context.name, last_header))
                last_header = current_header

            self.last_auto_contexts = None
            self.__ns[last_header] = {}
            return True
        else:
            return False

    def __match_contexts(self, input):
        match = self.platform_pattern.match(input)
        if match:        
            try:
                contexts = [GuiAutomationContext[n.upper()] for n in match.group(1).split(",")]
            except Exception as e:
                raise Exception("Invalid context name found in header: {}".format(e))
            else:
                for context in contexts:
                    if context in self.__ns[self.last_header]:
                        raise Exception("Found duplicate automation context {} in {} namespace definition.".format(context.name, self.last_header))
                    else:
                        self.__ns[self.last_header][context] = []
            
            self.last_auto_contexts = contexts
            return True
        else:
            return False

    def __match_locator(self, input):
        match = self.locator_pattern.match(input)
        if match:       
            locator = Locator(match.group(1), match.group(2))
            if (self.last_auto_contexts is None):
                raise Exception("Locators must be preceded with context information as #context1, context2 construct. Current line: " + input)   

            for context in self.last_auto_contexts:
                self.__ns[self.last_header][context].append(locator)
            return True
        else:
            return False

    def load(self):
        for line in self.__ns_file.readlines():
            if self.__match_header(line):
                self.header_found = True
                continue
            else:
                if not self.header_found:
                    raise Exception("Namespace contents must be contained inside a [name] header.")
                elif self.__match_contexts(line):
                    continue
                elif self.__match_locator(line):
                    continue
                else:
                    raise Exception("Unexpected namespace file entry. Namspace content can either be plaforms or identification definition: " + line)
        
        self.__ns_file.close()

        for ename, context_data in self.__ns.items():
            for context, locators in context_data.items():
                self.add_element_meta_data(ename, context, locators)

class GuiNamespaceLoaderFactory:

    # Returns GuiNamespaceLoader
    @classmethod
    def create_namespace_loader(cls, config, ns_file_path):
        _, file_extension = os.path.splitext(ns_file_path)
        ext = file_extension.upper()
        considered_path = ns_file_path
        try:
            file_format = FileFormat[ext]
        except:
            raise Exception("Unsupported format for namespace: {}".format(file_extension))
        else:
            ns_dir = config.value(SetuConfigOption.GUIAUTO_NAMESPACE_DIR)
            full_path = os.path.join(ns_dir, considered_path)
            full_file_path = os.path.abspath(full_path)
            if os.path.isdir(full_file_path):
                raise Exception("Namespace file path is a directory and not a file: {}".format(considered_path))
            elif not os.path.isfile(full_file_path):
                raise Exception("Namespace file path is invalid: {}".format(considered_path))

            if file_format == FileFormat.GNS:
                return NamespaceFileLoader(full_file_path)
            else:
                raise Exception("Unsupported format for namespace: {}".format(file_extension))

class Gui:

    def __init__(self, automator, file_def_path,*,  label=None):
        self.__automator = automator
        self.__file_def_path = file_def_path
        self.__children = []

    def add_child(self, label, file_def_path):
        self.__children.append(Gui(self.__automator, file_def_path, label=label))

class GuiFactory:

    @classmethod
    def create_app_from_dir(cls, name, automator, app_def_dir):
        considered_path = app_def_dir
        if not os.path.isdir(considered_path):
            ns_dir = automator.config.value(SetuConfigOption.GUIAUTO_NAMESPACE_DIR)
            full_path = os.path.join(ns_dir, considered_path)
            considered_path = os.path.abspath(full_path)
            if not os.path.isdir(considered_path):
                raise Exception("Provided root definition path is not a directory: {}".format(app_def_dir))

        app = Gui(automator, os.path.join(considered_path, "Home.gns"), label=name)
        children_dir = os.path.join(considered_path, "children")
        if os.path.isdir(children_dir):
            lfiles = os.listdir(children_dir)
            for f in lfiles:
                cpath = os.path.join(children_dir, f)
                if os.path.isfile(cpath):
                    base_name = os.path.basename(cpath)
                    app.add_child(base_name, cpath)

    @classmethod
    def create_gui(cls, automator, def_path):
        return Gui(automator, def_path)


    
        


    

