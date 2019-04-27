# CVSite Tom Saccasyn

Met behulp van dit GitHub project is het mogelijk om de code voor de site van Tom Saccasyn te verkrijgen.
Deze site is gemaakt voor het vak ITalent3 voor de Erasmushogeschool Brussel.

Met behulp van onderstaande uitleg kan het project worden gerund.

Om het project te kunnen runnen zal eerst python 3.7.3 moeten worden geïnstalleerd. 
De link om python te installeren staat hieronder:
https://www.python.org/downloads/release/python-373/

Als volgt zal het project moeten worden gedownload. 

In het project zal men moeten gaan naar de folder CV Site v2/CVSite2/CVSite2/ hierin zal men een commandoprompt moeten openen.
Het in volgend project zal men dan eerst moeten het volgende commando uitvoeren.
pip install flask
pip install flask-restful

Indien er een probleem is waardoor er telkens geprobeerd wordt om te "retry'en" zal volgend commando achter de vorige commando's moeten worden bijgezet.
--trusted-host pypi.org --trusted-host files.pythonhosted.org

Hierna kan men het project runnen door volgend commando in dezelfde folder als hierboven vermeld in te geven:
python runserver.py

Indien er men connectie wilt maken met de api, moet het project runnen. 
De api is aanspreekbaar door middel van een GET request. 
De api kan worden getest door de links op de Over Mij pagina uit te voeren in bijvoorbeeld Postman. 

Het bestand myapp.wsgi is een bestand dat ervoor zorgt dat het project zou kunnen draaien op een server indien men op deze server de mod mod_wsgi heeft geïnstalleerd.

