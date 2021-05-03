<?php
session_start(); 
?>
<!DOCTYPE html>
<html>
<head>
  <title>React! </title>
  <link href="https://unpkg.com/nes.css@2.3.0/css/nes.min.css" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"></link>
  <script
          src="https://code.jquery.com/jquery-3.1.1.min.js"
          integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
          crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.js"></script>
  <style>
    body {

      font-size:12pt;
    }
    html, body, pre, code, kbd, samp {
        font-family: "Press Start 2P";
    }
  </style>
</head>
<body>
  <?php
    if (isset($_SESSION['message']) && $_SESSION['message'])
    {
      printf('
      <dialog class="nes-dialog"  style="z-index:2;transform: translateY(30px);" open>
        <form method="dialog">
          <p>%s</p>
          <menu class="dialog-menu">
            <button class="nes-btn is-primary">OK</button>
          </menu>
        </form>
      </dialog>
      ', $_SESSION['message']);
      unset($_SESSION['message']);
    }
  ?>
  <div class="ui container" style="padding-top: 2%">
  <form method="POST" action="upload.php" enctype="multipart/form-data">
      <span>Upload your reaction images for storage in our high security server.  Never lose a meme again! </span>
    <div style="display:inline">

      <label class="nes-btn">
        <span>Select your file</span>
            <input type="file"  name="uploadedFile" />
      </label>
      <input type="submit" name="uploadBtn" class="nes-btn is-success" value="Upload" />
      <a href="uploads/" class="nes-btn is-primary">Uploaded Files</a>
    </div>


  </form>
</div>
</body>
</html>

