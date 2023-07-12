# Advanced Robotics (INFR112132022) tutorials

These instructions are written for ARO tutorials regarding set up on DICE environment.
A large part of these tutorials are adapted from [Nicolas Mansard's class at Supaero, 2023](https://github.com/Gepetto/supaero2023).

The exercices are organized by notebook. Each notebook corresponds to one chapter of the class.
The notebooks are in Python and based on the software [Pinocchio](https://github.com/stack-of-tasks/pinocchio).

## Set up 

### On a DICE machine
On DICE, the required dependencies to run the project are already available. 
You only need to "clone" the project to a local folder of your choice.
Open a terminal (CTRL + ALT + T) one and follow the commands below:

- `` cd ~``

  Move to home directory.


- `` git clone https://github.com/ediaro23/tutorials/``

    Clone the tutorials inside your home directory.

You should be done! See [below](#using-and-updating-the-notebooks) to check that your installation is working 

### Linux, Python 3, PyPI

On a Linux system with Python 3, you can get the dependencies directly with +[pip (see installation procedure and update below)](#installing-pip):
```bash
python3 -m pip install -r requirements.txt
```
NB: you should consider using a [virtualenv](https://docs.python.org/3/library/venv.html)

Once you have the dependencies, you can start the server with `jupyter notebook`

### Using Docker
TBD...

## Using and updating the notebooks
### Running a notebook
On your terminal, cd into the tutorials folder:
```bash
cd  ~/ediaro23/tutorials/
```
Now run Jupyter notebook with the command
```bash
jupyter notebook .
```
Click on '0_introduction_to_numerical_robotics.ipynb' to open the first notebook.

### Editing the notebook and updates
To avoid conflicts (see right after), it is recommended to make a local copy of a notebook before working on it.

If the repository changes (for example when new tutorials are pushed / a bug has been found), you will need to update your local
version by "pulling" it from the repository. On a native installation, just go in the folder containing the tutorials and execute ```git pull```


## Side notes

### Installing pip

Pip is a tool for installing and managing Python packages. You can install it with

```bash
sudo apt install python3-pip
```

The default version of +pip installed by +apt is not up to date, so upgrade it with
```bash
python3 -m pip install --upgrade --user
```

In general, running +pip is likely to run an alias on +pip in /usr, so either run it through python3 as explained above, or make sure your path select the right pip executable in your ~/.local. The option --user is kind of optional for recent +pip version, but removing it should work with a warning.

