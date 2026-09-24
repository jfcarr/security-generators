BASE_NAME_PASS=password_generator
BASE_NAME_PIN=pin_generator

default:
	@echo 'Targets:'
	@echo '  deploy'

make-executable:
	chmod u+x $(BASE_NAME_PASS).py
	chmod u+x $(BASE_NAME_PIN).py

deploy: make-executable
	cp $(BASE_NAME_PASS).py ~/bin/$(BASE_NAME_PASS)
	cp $(BASE_NAME_PIN).py ~/bin/$(BASE_NAME_PIN)
