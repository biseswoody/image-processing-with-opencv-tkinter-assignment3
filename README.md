# Image Processing Desktop Application

A comprehensive desktop image processing application built with Python, Tkinter, and OpenCV using object-oriented programming principles.

## Features

### Image Processing Operations
- **Grayscale Conversion**: Convert images to black and white
- **Blur Effect**: Apply Gaussian blur with adjustable intensity
- **Edge Detection**: Canny edge detection algorithm
- **Brightness Adjustment**: Real-time brightness control with slider
- **Contrast Adjustment**: Real-time contrast control with slider
- **Image Rotation**: Rotate images by 90°, 180°, and 270°
- **Image Flip**: Horizontal and vertical flipping
- **Resize/Rescale**: Graphical resize or enter custom dimensions

### GUI Components
- **Main Window**: Properly sized with appropriate title
- **Menu Bar**:
  - File menu (Open, Save, Save As, Exit)
  - Edit menu (Undo, Redo)
- **Image Display Area**: Canvas for image display
- **Control Panel**: Filter and effect options panel
- **Status Bar**: Current image information (filename, dimensions, etc.)

### File Operations
- Support for common image formats: PNG, JPEG, BMP
- File dialogs for opening and saving files
- Message boxes for confirmations and error handling

## Architecture

### Object-Oriented Design
The application follows OOP principles with proper encapsulation, constructors, methods, and class interactions:

```
ImageProcessorApp (Main Application)
├── ImageProcessor (Core Image Processing)
├── MenuManager (Menu Operations)
├── ControlPanel (Filter Controls)
├── ImageCanvas (Image Display)
└── StatusBar (Status Information)
```

### Class Structure

#### `ImageProcessor`
- Handles all OpenCV image processing operations
- Manages image state and history
- Provides methods for filters and transformations

#### `ImageProcessorApp`
- Main application class
- Coordinates between all components
- Manages the main window and layout

#### `MenuManager`
- Handles menu bar operations
- File operations (open, save, exit)
- Edit operations (undo, redo)

#### `ControlPanel`
- Manages all filter controls
- Sliders for brightness, contrast, blur
- Buttons for transformations

#### `ImageCanvas`
- Displays images on tkinter canvas
- Handles image scaling and fitting
- Manages canvas updates

#### `StatusBar`
- Displays current image information
- Shows filename, dimensions, and processing status

## Dependencies

The application uses UV for dependency management. Required packages:

- `opencv-python`: Image processing operations
- `Pillow`: Image format support and tkinter compatibility
- `numpy`: Numerical operations for image processing

## Installation and Setup

### Prerequisites
- Python 3.13 (required for tkinter compatibility)
- UV package manager installed

### Setup Instructions

1. **Clone or create the project directory**
2. **Initialize UV environment**:
   ```bash
   uv init
   ```

3. **Install dependencies**:
   ```bash
   uv add opencv-python Pillow numpy
   ```

4. **Run the application**:
   ```bash
   uv run python main.py
   ```

## Usage

1. **Open an Image**: Use File → Open or Ctrl+O
2. **Apply Filters**: Use the control panel to adjust brightness, contrast, blur
3. **Transform Image**: Use rotation and flip buttons
4. **Save Image**: Use File → Save or Ctrl+S
5. **Undo/Redo**: Use Edit menu or Ctrl+Z/Ctrl+Y

## Project Structure

```
image-processor/
├── README.md
├── pyproject.toml
├── main.py
├── src/
│   ├── __init__.py
│   ├── image_processor.py
│   ├── menu_manager.py
│   ├── control_panel.py
│   ├── image_canvas.py
│   └── status_bar.py
└── tests/
    └── test_image_processor.py
```

## Development Notes

### OOP Implementation
- **Encapsulation**: Each class manages its own state and methods
- **Constructors**: Proper initialization with required parameters
- **Class Interactions**: Clean interfaces between components
- **Inheritance**: Base classes for common functionality where applicable

### Error Handling
- File operation errors with user-friendly messages
- Image format validation
- Processing error handling

### Performance Considerations
- Efficient image processing with OpenCV
- Canvas update optimization
- Memory management for large images

# IMPORTANT: For macOS 26 and above using Homebrew build of python, which this application is tested in, make sure you set the python_version >= 3.13. Without this, the tkinter does not initialise, and the application fails.
