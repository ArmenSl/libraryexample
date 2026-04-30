####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Enumerations
Genre: Enumeration = Enumeration(
    name="Genre",
    literals={
            EnumerationLiteral(name="Poetry"),
			EnumerationLiteral(name="Thriller"),
			EnumerationLiteral(name="History"),
			EnumerationLiteral(name="Technology"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="Philosophy"),
			EnumerationLiteral(name="Cookbooks"),
			EnumerationLiteral(name="Fantasy")
    }
)

# Classes
Book = Class(name="Book")
Library = Class(name="Library")
Author = Class(name="Author")
Publisher = Class(name="Publisher")

# Book class attributes and methods
Book_title: Property = Property(name="title", type=StringType)
Book_pages: Property = Property(name="pages", type=IntegerType)
Book_stock: Property = Property(name="stock", type=IntegerType)
Book_price: Property = Property(name="price", type=FloatType)
Book_release: Property = Property(name="release", type=DateType)
Book_genre: Property = Property(name="genre", type=Genre)
Book_m_decrease_stock: Method = Method(name="decrease_stock", parameters={Parameter(name='qty', type=IntegerType)}, implementation_type=MethodImplementationType.CODE)
Book_m_decrease_stock.code = """def decrease_stock(self, qty: int):
    \"\"\"
    Decrease the available stock by the given quantity.

    :param qty: Number of items to remove from stock
    :raises ValueError: If qty is negative or exceeds available stock
    \"\"\"
    if qty <= 0:
        raise ValueError("Quantity must be a positive integer")

    if qty > self.stock:
        raise ValueError(
            f"Cannot decrease stock by {qty}. Only {self.stock} items available."
        )

    self.stock -= qty

"""
Book.attributes={Book_genre, Book_pages, Book_price, Book_release, Book_stock, Book_title}
Book.methods={Book_m_decrease_stock}

# Library class attributes and methods
Library_name: Property = Property(name="name", type=StringType)
Library_web_page: Property = Property(name="web_page", type=StringType)
Library_address: Property = Property(name="address", type=StringType)
Library_telephone: Property = Property(name="telephone", type=StringType)
Library_m_cheapest_book_by: Method = Method(name="cheapest_book_by", parameters={Parameter(name='author', type=Author)}, type=StringType, implementation_type=MethodImplementationType.BAL)
Library_m_cheapest_book_by.code = """def cheapest_book_by(author:Author) -> str {
    cheapest:Book = null;
	price = 1000000000.0;
	for(book in this.books){
        if(book.authors.contains(author)
			&& book.price <= price){
            cheapest = book;
			price = book.price;
		}
    }
	return cheapest.title;
}"""
Library.attributes={Library_address, Library_name, Library_telephone, Library_web_page}
Library.methods={Library_m_cheapest_book_by}

# Author class attributes and methods
Author_name: Property = Property(name="name", type=StringType)
Author_birth: Property = Property(name="birth", type=DateType)
Author.attributes={Author_birth, Author_name}

# Publisher class attributes and methods
Publisher_name: Property = Property(name="name", type=StringType)
Publisher_address: Property = Property(name="address", type=StringType)
Publisher_telephone: Property = Property(name="telephone", type=StringType)
Publisher.attributes={Publisher_address, Publisher_name, Publisher_telephone}

# Relationships
books: BinaryAssociation = BinaryAssociation(
    name="books",
    ends={
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
books_1: BinaryAssociation = BinaryAssociation(
    name="books_1",
    ends={
        Property(name="authors", type=Author, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
Publisher_Book: BinaryAssociation = BinaryAssociation(
    name="Publisher_Book",
    ends={
        Property(name="publisher", type=Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
constraint_Book_0_1: Constraint = Constraint(
    name="constraint_Book_0_1",
    context=Book,
    expression="context Book inv inv1: self.pages> 10",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Book, Library, Author, Publisher, Genre},
    associations={books, books_1, Publisher_Book},
    constraints={constraint_Book_0_1},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Book", view_elements=set(), is_main_page=True, route_path="/book", screen_size="Medium")
wrapper.component_id = "page-book-0"
i8hpu = Text(
    name="i8hpu",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i8hpu",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i8hpu"}
)
io3lx = Link(
    name="io3lx",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="io3lx",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "io3lx"}
)
i2wnl = Link(
    name="i2wnl",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i2wnl",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i2wnl"}
)
ixy5i = Link(
    name="ixy5i",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ixy5i",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "ixy5i"}
)
iq16r = Link(
    name="iq16r",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iq16r",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "iq16r"}
)
ilhxd = ViewContainer(
    name="ilhxd",
    description=" component",
    view_elements={io3lx, i2wnl, ixy5i, iq16r},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ilhxd",
    display_order=1,
    custom_attributes={"id": "ilhxd"}
)
ilhxd_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ilhxd.layout = ilhxd_layout
i8i9h = Text(
    name="i8i9h",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i8i9h",
    display_order=2,
    custom_attributes={"id": "i8i9h"}
)
iz92d = ViewContainer(
    name="iz92d",
    description="nav container",
    view_elements={i8hpu, ilhxd, i8i9h},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iz92d",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iz92d"}
)
iz92d_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iz92d.layout = iz92d_layout
i6nnd = Text(
    name="i6nnd",
    content="Book",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i6nnd",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i6nnd"}
)
iwall = Text(
    name="iwall",
    content="Manage Book data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iwall",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iwall"}
)
table_book_0_col_0 = FieldColumn(label="Title", field=Book_title)
table_book_0_col_1 = FieldColumn(label="Pages", field=Book_pages)
table_book_0_col_2 = FieldColumn(label="Stock", field=Book_stock)
table_book_0_col_3 = FieldColumn(label="Price", field=Book_price)
table_book_0_col_4 = FieldColumn(label="Release", field=Book_release)
table_book_0_col_5 = FieldColumn(label="Genre", field=Book_genre)
table_book_0_col_6_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "library")
table_book_0_col_6 = LookupColumn(label="Library", path=table_book_0_col_6_path, field=Library_name)
table_book_0_col_7_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "authors")
table_book_0_col_7 = LookupColumn(label="Authors", path=table_book_0_col_7_path, field=Author_name)
table_book_0 = Table(
    name="table_book_0",
    title="Book List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_book_0_col_0, table_book_0_col_1, table_book_0_col_2, table_book_0_col_3, table_book_0_col_4, table_book_0_col_5, table_book_0_col_6, table_book_0_col_7],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-book-0",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Book List", "data-source": "class_oho5ergc3_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'title', 'label': 'Title', 'columnType': 'field', '_expanded': False}, {'field': 'pages', 'label': 'Pages', 'columnType': 'field', '_expanded': False}, {'field': 'stock', 'label': 'Stock', 'columnType': 'field', '_expanded': False}, {'field': 'price', 'label': 'Price', 'columnType': 'field', '_expanded': False}, {'field': 'release', 'label': 'Release', 'columnType': 'field', '_expanded': False}, {'field': 'genre', 'label': 'Genre', 'columnType': 'field', '_expanded': False}, {'field': 'library', 'label': 'Library', 'columnType': 'lookup', 'lookupEntity': 'class_06blhjj3h_mjikkmod', 'lookupField': 'name', '_expanded': False}, {'field': 'authors', 'label': 'Authors', 'columnType': 'lookup', 'lookupEntity': 'class_d3f0di6lb_mjikkmoe', 'lookupField': 'name', '_expanded': False}, {'field': 'Publisher', 'label': 'Publisher', 'columnType': 'lookup', 'lookupEntity': 'class_lxo2luq0k_mol9ew72_ff2', 'lookupField': 'name', '_expanded': False}], "id": "table-book-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_book_0_binding_domain = None
if domain_model_ref is not None:
    table_book_0_binding_domain = domain_model_ref.get_class_by_name("Book")
if table_book_0_binding_domain:
    table_book_0_binding = DataBinding(domain_concept=table_book_0_binding_domain, name="BookDataBinding")
else:
    # Domain class 'Book' not resolved; data binding skipped.
    table_book_0_binding = None
if table_book_0_binding:
    table_book_0.data_binding = table_book_0_binding
ilrsy = Button(
    name="ilrsy",
    description="Button component",
    label="+ decrease_stock",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Book_m_decrease_stock,
    instance_source="table-book-0",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ilrsy",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ decrease_stock", "data-action-type": "run-method", "data-method": "method_rb01uirsh_mjikkmod", "data-instance-source": "table-book-0", "id": "ilrsy", "method-class": "Book", "endpoint": "/book/{book_id}/methods/decrease_stock/", "is-instance-method": "true", "input-parameters": {'qty': {'type': 'int', 'required': True}}, "instance-source": "table-book-0"}
)
iiiu2 = ViewContainer(
    name="iiiu2",
    description=" component",
    view_elements={ilrsy},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="iiiu2",
    display_order=3,
    custom_attributes={"id": "iiiu2"}
)
iiiu2_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
iiiu2.layout = iiiu2_layout
innow = ViewContainer(
    name="innow",
    description="main container",
    view_elements={i6nnd, iwall, table_book_0, iiiu2},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="innow",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "innow"}
)
innow_layout = Layout(flex="1")
innow.layout = innow_layout
iyzcz = ViewContainer(
    name="iyzcz",
    description=" component",
    view_elements={iz92d, innow},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iyzcz",
    display_order=0,
    custom_attributes={"id": "iyzcz"}
)
iyzcz_layout = Layout(layout_type=LayoutType.FLEX)
iyzcz.layout = iyzcz_layout
wrapper.view_elements = {iyzcz}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="Library", view_elements=set(), route_path="/library", screen_size="Medium")
wrapper_2.component_id = "page-library-1"
ij224 = Text(
    name="ij224",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ij224",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ij224"}
)
iehik = Link(
    name="iehik",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iehik",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "iehik"}
)
imey2 = Link(
    name="imey2",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imey2",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "imey2"}
)
ioyl3 = Link(
    name="ioyl3",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ioyl3",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "ioyl3"}
)
ijlp1 = Link(
    name="ijlp1",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ijlp1",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "ijlp1"}
)
i1map = ViewContainer(
    name="i1map",
    description=" component",
    view_elements={iehik, imey2, ioyl3, ijlp1},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i1map",
    display_order=1,
    custom_attributes={"id": "i1map"}
)
i1map_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i1map.layout = i1map_layout
ig85s = Text(
    name="ig85s",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ig85s",
    display_order=2,
    custom_attributes={"id": "ig85s"}
)
iu9p1 = ViewContainer(
    name="iu9p1",
    description="nav container",
    view_elements={ij224, i1map, ig85s},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iu9p1",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iu9p1"}
)
iu9p1_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iu9p1.layout = iu9p1_layout
i5tni = Text(
    name="i5tni",
    content="Library",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="i5tni",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i5tni"}
)
iitzh = Text(
    name="iitzh",
    content="Manage Library data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iitzh",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iitzh"}
)
table_library_1_col_0 = FieldColumn(label="Name", field=Library_name)
table_library_1_col_1 = FieldColumn(label="Web Page", field=Library_web_page)
table_library_1_col_2 = FieldColumn(label="Address", field=Library_address)
table_library_1_col_3 = FieldColumn(label="Telephone", field=Library_telephone)
table_library_1_col_4_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_library_1_col_4 = LookupColumn(label="Books", path=table_library_1_col_4_path, field=Book_title)
table_library_1 = Table(
    name="table_library_1",
    title="Library List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_library_1_col_0, table_library_1_col_1, table_library_1_col_2, table_library_1_col_3, table_library_1_col_4],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-library-1",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Library List", "data-source": "class_06blhjj3h_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'web_page', 'label': 'Web Page', 'columnType': 'field', '_expanded': False}, {'field': 'address', 'label': 'Address', 'columnType': 'field', '_expanded': False}, {'field': 'telephone', 'label': 'Telephone', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-library-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_library_1_binding_domain = None
if domain_model_ref is not None:
    table_library_1_binding_domain = domain_model_ref.get_class_by_name("Library")
if table_library_1_binding_domain:
    table_library_1_binding = DataBinding(domain_concept=table_library_1_binding_domain, name="LibraryDataBinding")
else:
    # Domain class 'Library' not resolved; data binding skipped.
    table_library_1_binding = None
if table_library_1_binding:
    table_library_1.data_binding = table_library_1_binding
ibp4c = Button(
    name="ibp4c",
    description="Button component",
    label="+ cheapest_book_by",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Library_m_cheapest_book_by,
    instance_source="table-library-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="ibp4c",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ cheapest_book_by", "data-action-type": "run-method", "data-method": "35ef5329-889b-40f0-89ce-9836936fd8a9", "data-instance-source": "table-library-1", "id": "ibp4c", "method-class": "Library", "endpoint": "/library/{library_id}/methods/cheapest_book_by/", "is-instance-method": "true", "input-parameters": {'author': {'type': 'Author', 'required': True, 'input_kind': 'lookup', 'entity': 'Author', 'lookup_field': 'name'}}, "instance-source": "table-library-1"}
)
imft6 = ViewContainer(
    name="imft6",
    description=" component",
    view_elements={ibp4c},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="imft6",
    display_order=3,
    custom_attributes={"id": "imft6"}
)
imft6_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
imft6.layout = imft6_layout
ija4p = ViewContainer(
    name="ija4p",
    description="main container",
    view_elements={i5tni, iitzh, table_library_1, imft6},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ija4p",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ija4p"}
)
ija4p_layout = Layout(flex="1")
ija4p.layout = ija4p_layout
i3x33 = ViewContainer(
    name="i3x33",
    description=" component",
    view_elements={iu9p1, ija4p},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i3x33",
    display_order=0,
    custom_attributes={"id": "i3x33"}
)
i3x33_layout = Layout(layout_type=LayoutType.FLEX)
i3x33.layout = i3x33_layout
wrapper_2.view_elements = {i3x33}


# Screen: wrapper_3
wrapper_3 = Screen(name="wrapper_3", description="Author", view_elements=set(), route_path="/author", screen_size="Medium")
wrapper_3.component_id = "page-author-2"
i9g4s = Text(
    name="i9g4s",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i9g4s",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i9g4s"}
)
iwlxp = Link(
    name="iwlxp",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iwlxp",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "iwlxp"}
)
i8vnt = Link(
    name="i8vnt",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8vnt",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i8vnt"}
)
i1458 = Link(
    name="i1458",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i1458",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "i1458"}
)
inc3w = Link(
    name="inc3w",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="inc3w",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "inc3w"}
)
iq2rh = ViewContainer(
    name="iq2rh",
    description=" component",
    view_elements={iwlxp, i8vnt, i1458, inc3w},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iq2rh",
    display_order=1,
    custom_attributes={"id": "iq2rh"}
)
iq2rh_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iq2rh.layout = iq2rh_layout
i4bsq = Text(
    name="i4bsq",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i4bsq",
    display_order=2,
    custom_attributes={"id": "i4bsq"}
)
im3tq = ViewContainer(
    name="im3tq",
    description="nav container",
    view_elements={i9g4s, iq2rh, i4bsq},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="im3tq",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "im3tq"}
)
im3tq_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
im3tq.layout = im3tq_layout
iefez = Text(
    name="iefez",
    content="Author",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iefez",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iefez"}
)
ifiay = Text(
    name="ifiay",
    content="Manage Author data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ifiay",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ifiay"}
)
table_author_2_col_0 = FieldColumn(label="Name", field=Author_name)
table_author_2_col_1 = FieldColumn(label="Birth", field=Author_birth)
table_author_2_col_2_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_author_2_col_2 = LookupColumn(label="Books", path=table_author_2_col_2_path, field=Book_title)
table_author_2 = Table(
    name="table_author_2",
    title="Author List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_author_2_col_0, table_author_2_col_1, table_author_2_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-author-2",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Author List", "data-source": "class_d3f0di6lb_mjikkmoe", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'birth', 'label': 'Birth', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-author-2", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_author_2_binding_domain = None
if domain_model_ref is not None:
    table_author_2_binding_domain = domain_model_ref.get_class_by_name("Author")
if table_author_2_binding_domain:
    table_author_2_binding = DataBinding(domain_concept=table_author_2_binding_domain, name="AuthorDataBinding")
else:
    # Domain class 'Author' not resolved; data binding skipped.
    table_author_2_binding = None
if table_author_2_binding:
    table_author_2.data_binding = table_author_2_binding
i3m22 = ViewContainer(
    name="i3m22",
    description="main container",
    view_elements={iefez, ifiay, table_author_2},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i3m22",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i3m22"}
)
i3m22_layout = Layout(flex="1")
i3m22.layout = i3m22_layout
idw9v = ViewContainer(
    name="idw9v",
    description=" component",
    view_elements={im3tq, i3m22},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="idw9v",
    display_order=0,
    custom_attributes={"id": "idw9v"}
)
idw9v_layout = Layout(layout_type=LayoutType.FLEX)
idw9v.layout = idw9v_layout
wrapper_3.view_elements = {idw9v}


# Screen: wrapper_4
wrapper_4 = Screen(name="wrapper_4", description="Publisher", view_elements=set(), route_path="/publisher", screen_size="Medium")
wrapper_4.component_id = "page-publisher-3"
iyjwc = Text(
    name="iyjwc",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="iyjwc",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iyjwc"}
)
i8sjc = Link(
    name="i8sjc",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i8sjc",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i8sjc"}
)
iofb9u = Link(
    name="iofb9u",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iofb9u",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "iofb9u"}
)
i63azg = Link(
    name="i63azg",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i63azg",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "i63azg"}
)
ilpdqt = Link(
    name="ilpdqt",
    description="Link element",
    label="Publisher",
    url="/publisher",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ilpdqt",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/publisher", "id": "ilpdqt"}
)
inqme = ViewContainer(
    name="inqme",
    description=" component",
    view_elements={i8sjc, iofb9u, i63azg, ilpdqt},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="inqme",
    display_order=1,
    custom_attributes={"id": "inqme"}
)
inqme_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
inqme.layout = inqme_layout
is93vh = Text(
    name="is93vh",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="is93vh",
    display_order=2,
    custom_attributes={"id": "is93vh"}
)
inkpt = ViewContainer(
    name="inkpt",
    description="nav container",
    view_elements={iyjwc, inqme, is93vh},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="inkpt",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "inkpt"}
)
inkpt_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
inkpt.layout = inkpt_layout
iddril = Text(
    name="iddril",
    content="Publisher",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iddril",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iddril"}
)
i7hhsi = Text(
    name="i7hhsi",
    content="Manage Publisher data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="i7hhsi",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "i7hhsi"}
)
table_publisher_3_col_0 = FieldColumn(label="Name", field=Publisher_name)
table_publisher_3_col_1 = FieldColumn(label="Address", field=Publisher_address)
table_publisher_3_col_2 = FieldColumn(label="Telephone", field=Publisher_telephone)
table_publisher_3 = Table(
    name="table_publisher_3",
    title="Publisher List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_publisher_3_col_0, table_publisher_3_col_1, table_publisher_3_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-publisher-3",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Publisher List", "data-source": "class_lxo2luq0k_mol9ew72_ff2", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'address', 'label': 'Address', 'columnType': 'field', '_expanded': False}, {'field': 'telephone', 'label': 'Telephone', 'columnType': 'field', '_expanded': False}, {'field': 'Book', 'label': 'Book', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-publisher-3", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_publisher_3_binding_domain = None
if domain_model_ref is not None:
    table_publisher_3_binding_domain = domain_model_ref.get_class_by_name("Publisher")
if table_publisher_3_binding_domain:
    table_publisher_3_binding = DataBinding(domain_concept=table_publisher_3_binding_domain, name="PublisherDataBinding")
else:
    # Domain class 'Publisher' not resolved; data binding skipped.
    table_publisher_3_binding = None
if table_publisher_3_binding:
    table_publisher_3.data_binding = table_publisher_3_binding
ig2kx7 = ViewContainer(
    name="ig2kx7",
    description="main container",
    view_elements={iddril, i7hhsi, table_publisher_3},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ig2kx7",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ig2kx7"}
)
ig2kx7_layout = Layout(flex="1")
ig2kx7.layout = ig2kx7_layout
igvsn = ViewContainer(
    name="igvsn",
    description=" component",
    view_elements={inkpt, ig2kx7},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="igvsn",
    display_order=0,
    custom_attributes={"id": "igvsn"}
)
igvsn_layout = Layout(layout_type=LayoutType.FLEX)
igvsn.layout = igvsn_layout
wrapper_4.view_elements = {igvsn}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_2, wrapper_3, wrapper_4}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
