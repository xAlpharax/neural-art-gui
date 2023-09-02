# neural-art-gui

Extension to the [neural-art](https://github.com/xAlpharax/neural-art) repo, serving as a GUI frontend.

Setup is done via virtualenv. Made with PySide6 and qtdarktheme and some other tweaks(seen in `./changes`) to get it working nicely.

## Requirements and Setup

Clone the repository and cd into it:

```bash
git clone https://github.com/xAlpharax/neural-art-gui ; cd neural-art-gui
```

Make a new virtualenv:

```bash
# Creating
virtualenv .

# Activating
source bin/activate
```

Setup all requirements.

```bash
pip install -r requirements.txt
```

Everything should now work as intended.

## Running the GUI

It is as simple as running:

```bash
python actual-gui.py
```

### Development

You can see changes that differ in the neural-art directory from the main repo in the `./changes` file.

Helper scripts for qtdesigner and it's xml > py tool can be found in `./designer` and `./designer2python`

### Todo

Make the neural-art dir a submodule OR, alternatively, make a new branch in the main repo to house these diffs.
