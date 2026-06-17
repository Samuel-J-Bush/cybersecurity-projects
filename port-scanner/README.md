# Port Scanner Project

Python file to detect any open ports from the dictionary of commonly vulnreable ports.

## What it does:
* Receives input of target (scanme).
* Attemps to secure a commection with the listed ports.
* Outputs any open ports.

## TCP Socket:
* A TCP socket is used for attempting to connect to port.
* Timeout is set to 1 second.
* If the port is open, a connection will be established: function returns True.
* If the port is closed, a connection wont be established: function returns False.

## What I learnt:
* Ports.
	* Uses and relevance to security.
	* Commonly targeted ports. 
* Python Logic.
	* Definite iteration.
	* Selection. 
	* F string output.

   ## Disclaimer:
  This is an educational project for scanning practice sites or personal devices. Scanning devices or sites unauthorised is illegal.
