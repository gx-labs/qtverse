class CustomListWidgetItem(QWidget):
    folderClicked = Signal(str)

    def __init__(self, name, path, status_color):
        super().__init__()

        self.folder_path = path

        self.main_layout = QHBoxLayout(self)

        # Foldername label
        self.foldername_label = ClickableLabel(name)
        self.main_layout.addWidget(self.foldername_label)

        # Category label
        self.category_label = QLabel()
        self.main_layout.addWidget(self.category_label)

        # Status label
        self.status_label = QLabel()
        self.status_label.setFont(QFont("Arial", 11, QFont.Bold))
        self.status_label.setStyleSheet(f"color: {status_color};")
        self.main_layout.addWidget(self.status_label)

        # Add context menu to the custom widget
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # get status of Custom Widget from info.yaml                                
        info_filepath = os.path.join(self.folder_path, "info.yaml")
        info_data = read_yaml(filepath=info_filepath)                        

        self.category_label.setText(f"{info_data.get('category')}") 
        self.status_label.setText(f"{info_data.get('status')}")

    def show_context_menu(self, position):
        menu = QMenu(self)

        # Create actions for the context menu
        wip_action = QAction("wip", self)
        submitted_action = QAction("submitted", self)
        review_action = QAction("review", self)
        approved_action = QAction("approved", self)

        # Connect actions to update info.yaml and the displayed status label
        wip_action.triggered.connect(lambda: self.update_yaml("wip"))
        submitted_action.triggered.connect(lambda: self.update_yaml("submitted"))
        review_action.triggered.connect(lambda: self.update_yaml("review"))
        approved_action.triggered.connect(lambda: self.update_yaml("approved"))

        # Add actions to the menu
        menu.addAction(wip_action)
        menu.addAction(submitted_action)
        menu.addAction(review_action)
        menu.addAction(approved_action)

        # Show the context menu
        menu.exec_(self.mapToGlobal(position))

    def update_yaml(self, new_status):
        info_yaml_file_path = os.path.join(self.folder_path, "info.yaml")
        if os.path.exists(info_yaml_file_path):
            # Reading information from info.yaml using read_yaml function
            info_data = read_yaml(info_yaml_file_path)

            # Update the status in the info data
            info_data['status'] = new_status

            # Write the updated info data back to the info.yaml file
            with open(info_yaml_file_path, 'w') as file:
                yaml.dump(info_data, file)

            # Update the displayed status label
            self.status_label.setText(f"{new_status}")

# Filters ----------
        self.filter_widget = QWidget()
        self.filter_widget.setContentsMargins(0,0,0,0)

        self.filter_layout = QHBoxLayout()
        self.filter_widget.setLayout(self.filter_layout)
        
        # groupbox 
        self.groupbox = QGroupBox()
       
        self.groupbox_layout = QHBoxLayout(self.groupbox)
        self.all_button = QPushButton("ALL")
        self.groupbox_layout.addWidget(self.all_button)
        self.all_button.clicked.connect(lambda: self.filter_by_developer("ALL"))

        self.esh_button = QPushButton("ESH")
        self.groupbox_layout.addWidget(self.esh_button)
        self.esh_button.clicked.connect(lambda: self.filter_by_developer("ESH"))

        self.prt_button = QPushButton("PRT")
        self.groupbox_layout.addWidget(self.prt_button)
        self.prt_button.clicked.connect(lambda: self.filter_by_developer("PRT"))

        self.sam_button = QPushButton("SAM")
        self.groupbox_layout.addWidget(self.sam_button)
        self.sam_button.clicked.connect(lambda: self.filter_by_developer("SAM"))

        self.shb_button = QPushButton("SHB")
        self.groupbox_layout.addWidget(self.shb_button)
        self.shb_button.clicked.connect(lambda: self.filter_by_developer("SHB"))

        # status buttons
        self.statusButton_layout = QHBoxLayout()

        self.wip = QPushButton("wip")
        self.wip.setFlat(True)
        self.wip.setFont(QFont("Arial", 11, QFont.Bold))
        self.wip.setStyleSheet(f"color: { STATUS_COLOR_MAP.get('wip')};") 
        self.statusButton_layout.addWidget(self.wip)
        self.wip.clicked.connect(lambda: self.filter_by_status("wip"))
        
        self.submitted = QPushButton("submitted")
        self.submitted.setFlat(True)
        self.submitted.setFont(QFont("Arial", 11, QFont.Bold))
        self.submitted.setStyleSheet(f"color: { STATUS_COLOR_MAP.get('submitted')};") 
        self.statusButton_layout.addWidget(self.submitted)
        self.submitted.clicked.connect(lambda: self.filter_by_status("submitted"))
        
        self.review = QPushButton("review")
        self.review.setFlat(True)
        self.review.setFont(QFont("Arial", 11, QFont.Bold))
        self.review.setStyleSheet(f"color: { STATUS_COLOR_MAP.get('review')};") 
        self.statusButton_layout.addWidget(self.review)
        self.review.clicked.connect(lambda: self.filter_by_status("review"))
        
        self.approved = QPushButton("approved")
        self.approved.setFlat(True)
        self.approved.setFont(QFont("Arial", 11, QFont.Bold))
        self.approved.setStyleSheet(f"color: { STATUS_COLOR_MAP.get('approved')};") 
        self.statusButton_layout.addWidget(self.approved)
        self.approved.clicked.connect(lambda: self.filter_by_status("approved"))


        self.filter_layout.addWidget(self.groupbox)  
        self.filter_layout.addLayout(self.statusButton_layout)

        self.vertical_layout.addWidget(self.filter_widget)

        # -----------------------
        self.list_layout = QHBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.setMaximumWidth(400)
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        self.contents_widget = QWidget()
        self.contents_layout = QVBoxLayout()
        self.contents_widget.setLayout(self.contents_layout)

        self.list_layout.addWidget(self.list_widget)
        self.list_layout.addWidget(self.contents_widget)