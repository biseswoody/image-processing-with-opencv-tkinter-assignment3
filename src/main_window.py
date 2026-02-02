import tkinter as tk
from tkinter import ttk
import numpy as np
from .image_processor import ImageProcessor
from typing import Callable

# PLEASE REFER TO THE REFERENCE UI SCREENSHOT BEFORE YOU WORK ON YOUR SECTIONS


# SET 2 - TBD: Aryan
class ImageCanvas:
    """Image canvas component that displays the image canvas"""

    def __init__(self, parent: tk.Widget, width: int = 800, height: int = 600):
        """Initialise the image canvas where image is loaded & worked on

        Args:
            parent: parent container Widget
            width: canvas width
            height: canvas height

        """

    def display_image(self, image: np.ndarray) -> None:
        """Display an image on the created canvas

        Args:
            image: OpenCV array of image pixels

        """
        # Important - handle all exceptions here, there may be errors

    def clear_canvas(self) -> None:
        """Clear the canvas"""

    def get_display_scale(self) -> float:
        """Get current display scale factor. Important for efficient window management, menu layout and other transformations"""



# Set 3 - TBD: Bishesh
class StatusBar:
    """Status bar component for displaying image metadata"""

    def __init__(self, parent: tk.Widget):
        """Initialise the status bar

        Args:
            parent: Parent tkinter widget
        """

    def update_metadata(self, filename: str, dimensions: tuple, format_name: str) -> None:
        """Update the status bar metadata of the image IF the image changes

        Args:
            filename: Image filename,
            dimensions: Tuple(width: int, height: int)
            format_name: Image format

        """


# Set 4 - TBD: Yasmeen
class MenuManager:
    """Menu bar management."""

    def __init__(
        self, root: tk.Tk, processor: ImageProcessor, update_callback: Callable
    ):
        """
        Initialize menu manager on the top of the screen

        Args:
            root: Root window
            processor: ImageProcessor instance
            update_callback: Callback to update display. A function argument is needed here
        """

    def _create_file_menu(self) -> None:
        """Create file menu."""

    def _create_edit_menu(self) -> None:
        """Create edit menu."""

    def _open_file(self) -> None:
        """Open file dialog."""

    def _save_file(self) -> None:
        """Save current image on the same base file"""

    def _save_as_file(self) -> None:
        """Save current image with new filename"""

    def _undo(self) -> None:
        """Undo last operation"""

    def _redo(self) -> None:
        """Redo last undone operation"""


# Set 5 - TBD: Sandeep
class ControlPanel:
    """Control panel for filters and effects."""

    def __init__(
        self, parent: tk.Widget, processor: ImageProcessor, update_callback: Callable
    ):
        """
        Initialize control panel.

        Args:
            parent: Parent widget
            processor: ImageProcessor instance
            update_callback: Callback to update display
        """

    def _create_basic_controls(self) -> None:
        """Create basic filter controls"""

    def _create_adjustment_controls(self) -> None:
        """Create adjustment sliders"""

    def _create_transform_controls(self) -> None:
        """Create transformation controls"""

    def _create_resize_controls(self) -> None:
        """Create resize controls"""

    def _apply_grayscale(self) -> None:
        """Apply grayscale filter"""

    def _apply_edge_detection(self) -> None:
        """Apply edge detection filter"""

    def _rotate_image(self, angle: int) -> None:
        """Rotate image by specified angle"""

    def _flip_image(self, direction: str) -> None:
        """Flip image in specified direction"""

    def _resize_image(self) -> None:
        """Resize image to specified dimensions"""

    def _start_blur_adjustment(self) -> None:
        """Start blur adjustment, save base state only if not already adjusting blur."""

    def _on_blur_preview(self) -> None:
        """Preview blur while dragging."""

    def _finish_blur_adjustment(self) -> None:
        """Finish blur adjustment - commit to history, BUTTTTTT keep the base for further adjustments"""

    def _start_brightness_adjustment(self) -> None:
        """Start brightness adjustment - save base state"""

    def _on_brightness_preview(self) -> None:
        """Preview brightness while dragging"""

    def _finish_brightness_adjustment(self) -> None:
        """Finish brightness adjustment - commit to history"""

    def _start_contrast_adjustment(self) -> None:
        """Start contrast adjustment - save base state"""

    def _on_contrast_preview(self) -> None:
        """Preview contrast while dragging"""

    def _finish_contrast_adjustment(self) -> None:
        """Finish contrast adjustment - commit to history"""

    def _reset_image(self) -> None:
        """Reset image to original state"""


# SET 1 - TBD: Sandeep
class ImageProcessorApp:
    """This is the main application class, initialised by main"""

    def __init__(self):
        """Initialisation happens here."""
        self.root = tk.Tk()
        self.root.title("Image Processor")
        self.root.geometry("1000x800")
        self.root.minsize(800,600)

        self.processor = ImageProcessor()

        self._create_widgets()
        self._setup_layout()
        self._update_display()

    def _create_widgets(self) -> None:
        """All GUI components need to be created here"""
        # Things to be done:

        # 0. Create main container first, actually
        # IMPORTANT: ttk, NOT tk. ttk = Themed TK, perfect for native look/feel
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # 1. Create control panel
        self.control_panel = ControlPanel(self.main_container, self.processor, self._update_display)

        # 2. Create image canvas
        self.image_canvas = ImageCanvas(self.main_container)

        # 3. Create menu manager
        self.menu_manager = MenuManager(self.root, self.processor, self._update_display)

        # 4. Create Status bar
        self.status_bar = StatusBar(self.root)

        # 5. My bad I'm dumb - no need to add everything to root, since main_container is passed already to each widget function

    def _setup_layout(self) -> None:
        """Setup the layout here"""
        # Things to be done:
        # 1. ControlPanel constructor to pack the control to left - TBD: to be implemented in the ControlPanel constructor, NOT here
        # 2. Pack the canvas to fill the rest of the space
        self.image_canvas.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _update_display(self) -> None:
        """Update the image display and status bar"""
        # Things to be done:
        # 1. Get current image and set it to the current image in canvas, basically live rendering on changes
        current_image = self.processor.get_current_image()
        self.image_canvas.display_image(current_image)
        # 2. Display filename, dimension, format as needed
        filename, dimensions, format_name = self.processor.get_image_info()
        self.status_bar.update_info(filename, dimensions, format_name)

    def run(self) -> None:
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = ImageProcessorApp()
    app.run()
