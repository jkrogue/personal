<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<link rel="shortcut icon" href="images/reviewer.ico" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>Reviewer</title>
<meta name="Generator" content="Cocoa HTML Writer">
<meta name="CocoaVersion" content="1187.34">
<style type="text/css">
p.p1 {margin: 0.0px 0.0px 12.0px 0.0px; font: 12.0px Times; color: #0000ee}
    span.s1 {text-decoration: underline}
    </style>
    
    <script language="javascript" type="text/javascript">
    function selectAll(id){
        document.getElementById(id).focus();
        document.getElementById(id).select();
    }
    </script>
    
</head>
<body>

    <?PHP
    if(isset($_POST['submit'])){
        function makeDate($date){
            $month = substr($date, 0, 2);
            $day = substr($date, 2, 2);
            $year = substr($date, 4, 4);
            return mktime(0,0,0,$month,$day,$year);
        }
        
        function processForm($origDate){
            $potentialFiles = getPotentialFiles($origDate);
            linkToActualFiles($potentialFiles);
            echo("<p>Do another? <input type=\"button\" value=\"Yes\" onclick=\"parent.location='http://reviewer.hostoi.com/'\" /></p>");
        }
        
        function getPotentialFiles($origDate){
            $potentialFiles = array();
            $index = 0;
            
            $curDate = $origDate;
            
            //yesterday
            $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 1,date("Y",$curDate));
            $potentialFiles[$index++] = date("mdY", $curDate);
            
            //every other day for a week
            for ($i = 0; $i < 3; $i++){
                $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 2,date("Y",$curDate));
                $potentialFiles[$index++] = date("mdY", $curDate);
            }
            
            //once a week later
            $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 7,date("Y",$curDate));
            $potentialFiles[$index++] = date("mdY", $curDate);
            
            //once 2 weeks later
            $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 14,date("Y",$curDate));
            $potentialFiles[$index++] = date("mdY", $curDate);
            
            //every month for 2 months
            for ($i = 0; $i < 2; $i++){
                $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 28,date("Y",$curDate));
                $potentialFiles[$index++] = date("mdY", $curDate);
            }
            
            //every month for 10 months
            for ($i = 0; $i < 5; $i++){
                $curDate = mktime(0,0,0,date("m",$curDate),date("d",$curDate) - 56,date("Y",$curDate));
                $potentialFiles[$index++] = date("mdY", $curDate);
            }
            
            
            /*Uncomment to print out list of files that should be checked
             for ($i = 0; $i < count($potentialFiles); $i++){
             echo("$potentialFiles[$i]<br />");
             }*/
            
            return $potentialFiles;
        }
        
        function linkToActualFiles($potentialFiles){
            $directory = "https://dl.dropbox.com/u/80585765/reviewer/";
            $extension = ".htm";
            
            for ($i = 0; $i < count($potentialFiles); $i++){
                $url = $directory . $potentialFiles[$i] . $extension;
                if (exists($url))
                    echo ("<a href=\"" . $url . "\" + target=\"_blank\">" . date("m/d/Y", makeDate($potentialFiles[$i])) . "</a><br />");
            }
        }
        
        function exists($url){
            $url = @parse_url($url);
            if (!$url) return false;
            
            $url = array_map('trim', $url);
            $url['port'] = (!isset($url['port'])) ? 80 : (int)$url['port'];
            
            $path = (isset($url['path'])) ? $url['path'] : '/';
            $path .= (isset($url['query'])) ? "?$url[query]" : '';
            
            if (isset($url['host']) && $url['host'] != gethostbyname($url['host'])) {
                
                $fp = fsockopen($url['host'], $url['port'], $errno, $errstr, 30);
                
                if (!$fp) return false; //socket not opened
                
                fputs($fp, "HEAD $path HTTP/1.1\r\nHost: $url[host]\r\n\r\n"); //socket opened
                $headers = fread($fp, 4096);
                fclose($fp);
                
                if(preg_match('#^HTTP/.*\s+[(200|301|302)]+\s#i', $headers)){//matching header
                    return true;
                }
                else return false;
                
            } // if parse url
            else return false;
        }

        $month = $_POST['month'];
        $day = $_POST['day'];
        $year = $_POST['year'];
        //echo("$date");
        
        $origDate = mktime(0,0,0,$month,$day,$year);
        echo("<p>Review files for " . date("m/d/Y", $origDate) . ": </p>");
        
        
        processForm($origDate);
        
    }
    else{
        $month = date("m");
        $day = date("d");
        $year = date("Y");?>

        <form name="form" id="form" action="index.php" method="post">
            <p>Enter today's date:
        
            <input type="text" name="month" id="txt_month" size="2" value=<?php echo $month;?> onclick="selectAll('txt_month');"/>
            <input type="text" name="day" id="txt_day" size="2" value=<?php echo $day;?>  onclick="selectAll('txt_day');"/ />
            <input type="text" name="year" id="txt_year" size="4" value=<?php echo $year;?>  onclick="selectAll('txt_year');"/ />
        
            <input type="submit" name="submit" value="Submit" />
        
            </p>
        </form>
        <?PHP
    }?>
</body>
</html>
