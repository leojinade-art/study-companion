from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
    QApplication,
)

from logic.logic_controller import process_text


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Study Companion")
        self.resize(900, 700)

        self.current_file_name = "No file loaded"

        


        main_layout = QVBoxLayout()

        # Top actions
        top_bar = QHBoxLayout()

        

        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.load_file)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_all)

        top_bar.addWidget(self.upload_button)
        top_bar.addWidget(self.clear_button)

        # File name label
        self.file_label = QLabel(f"File: {self.current_file_name}")

        # Input section
        self.input_label = QLabel("Study Material")
        self.input = QTextEdit()
        self.input.setPlaceholderText("Upload a TXT file or paste text here...")

        # Action buttons
        action_bar = QHBoxLayout()

        self.explain_button = QPushButton("Explain")
        self.explain_button.clicked.connect(lambda: self.run_ai("Explain"))

        self.summarize_button = QPushButton("Summarize")
        self.summarize_button.clicked.connect(lambda: self.run_ai("Summarize"))

        self.keywords_button = QPushButton("Keywords")
        self.keywords_button.clicked.connect(lambda: self.run_ai("Keywords"))

         # save file
        self.save_button = QPushButton("Save Output")
        self.save_button.clicked.connect(self.save_output)

        action_bar.addWidget(self.explain_button)
        action_bar.addWidget(self.summarize_button)
        action_bar.addWidget(self.keywords_button)
        action_bar.addWidget(self.save_button)
        
        # Output section
        self.output_label = QLabel("Assistant Response")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Select text above, then choose an action.")

        main_layout.addLayout(top_bar)
        main_layout.addWidget(self.file_label)
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input)
        main_layout.addLayout(action_bar)
        main_layout.addWidget(self.output_label)
        main_layout.addWidget(self.output)

        self.setLayout(main_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt)"
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.input.setText(content)

                file_name = file_path.split("/")[-1].split("\\")[-1]
                self.current_file_name = file_name
                self.file_label.setText(f"File: {self.current_file_name}")
                self.output.setText("File loaded. Select part of the text and choose an action.")
            except Exception as e:
                self.output.setText(f"Error loading file: {e}")

    def clear_all(self):
        self.input.clear()
        self.output.clear()
        self.current_file_name = "No file loaded"
        self.file_label.setText(f"File: {self.current_file_name}")

    def save_output(self):
        output_text = self.output.toPlainText()

        if not output_text.strip():
            self.output.setText("Nothing to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Output",
            "assistant_response.txt",
            "Text Files (*.txt)"
        )

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(output_text)
                self.output.setText("Output saved successfully.")
            except Exception as e:
                self.output.setText(f"Error saving file: {e}")

    def run_ai(self, mode):
        cursor = self.input.textCursor()

        #guards for text selecting
        if not cursor.hasSelection():
            self.output.setText("Please select part of the text first.")
            return

        selected_text = cursor.selectedText()

        if not selected_text.strip():
            self.output.setText("Selected text is empty.")
            return

        self.output.setText("Working...")
        QApplication.processEvents()

        result = process_text(mode, selected_text, self.current_file_name)
        self.output.setText(result)