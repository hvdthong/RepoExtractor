![Alt text](https://github.com/CoolerVoid/raptor_waf/blob/master/doc/images/raptor2.png)
# raptor_waf

Raptor is a Web application firewall made in C, uses DFA to block SQL injection, Cross site scripting and path traversal.
http://funguscodes.blogspot.com.br/

# THis is PoC version
![Alt text](https://github.com/CoolerVoid/raptor_waf/blob/master/doc/images/help.png)

# to run:
$ git clone https://github.com/CoolerVoid/raptor_waf

$ cd raptor_waf; make; bin/raptor

#Note:
Don't execute with "cd bin; ./raptor" use full path "bin/raptor" look detail https://github.com/CoolerVoid/raptor_waf/issues/4

Need lib pcre to  compile.


# Example

Up some HTTPd server at port 80 
redirect with raptor to port 8883

$ bin/Raptor -h localhost -p 80 -r 8883 -w 4 -o loglog.txt

Copy vulnerable PHP code to your web server directory

$ cp doc/test_dfa/test.php /var/www/html

Now you can test xss attacks at 
http://localhost:8883/test.php

Other option to run(now with regex, look file config/regex_rules.txt to edit rules):

$ bin/Raptor -h 127.0.0.1 -p 80 -r 8883 -w 0 -o resultwaf -m pcre

# Look the docs

https://github.com/CoolerVoid/raptor_waf/blob/master/doc/raptor.pdf
