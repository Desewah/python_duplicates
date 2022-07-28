<?php
    $FileName = $_FILES['bar']['name'];
    $TmpName = $_FILES['bar']['tmp_name'];

    move_uploaded_file($TmpName, $FileName);

    echo("File Uploaded Successfully");
?>