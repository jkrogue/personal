sh compile.sh
cd ../src
jar cvfm "Reviewer.jar" manifest.txt med/reviewer/*.class med/utils/*.class
mv Reviewer.jar ../Reviewer.jar
cd ../scripts
