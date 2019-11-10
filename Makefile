main:
	python -m roadmaps

app:
	python -m roadmaps.webapp

test:
	python -m unittest discover -t roadmaps -s roadmaps/tests