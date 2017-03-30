cd C:\Users\HZMMIC02\Documents\python\Aqserver\doc
cd de
call make clean      
call make html      
rem call make dirhtml   
call make singlehtml
rem call make pickle    
rem call make json      
call make htmlhelp  
rem call make qthelp    
rem call make devhelp   
call make epub      
call make latex     
rem call make text      
rem call make man       
rem call make texinfo   
rem call make gettext   
rem call make changes   
rem call make xml       
rem call make pseudoxml 
rem call make linkcheck 
rem call make doctest   
rem call make coverage  
cd ../en
call make clean      
call make html      
rem call make dirhtml   
call make singlehtml
rem call make pickle    
rem call make json      
call make htmlhelp  
rem call make qthelp    
rem call make envhelp   
call make epub      
call make latex     
rem call make text      
rem call make man       
rem call make texinfo   
rem call make gettext   
rem call make changes   
rem call make xml       
rem call make pseudoxml 
rem call make linkcheck 
rem call make doctest   
rem call make coverage  

rem make PDF from tex
cd C:\Users\HZMMIC02\Documents\python\Aqserver\doc
call tex
rem compile htmlhelp
cd C:\Users\HZMMIC02\Documents\python\Aqserver\doc
call chm
pause
