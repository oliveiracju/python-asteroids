# Makefile

# Create a virtual environment and install dependencies
setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Run the project
run:
	. venv/bin/activate && python3 ./app/main.py

# Clean up the virtual environment
clean:
	rm -rf venv