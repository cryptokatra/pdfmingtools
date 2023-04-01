import streamlit as st

# CSS
st.write(
    """
    <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      margin: 0;
    }

    .navbar {
      overflow: hidden;
      background-color: #333;
    }

    .navbar a {
      float: left;
      font-size: 16px;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }

    .subnav {
      float: left;
      overflow: hidden;
    }

    .subnav .subnavbtn {
      font-size: 16px;
      border: none;
      outline: none;
      color: white;
      padding: 14px 16px;
      background-color: inherit;
      font-family: inherit;
      margin: 0;
    }

    .navbar a:hover,
    .subnav:hover .subnavbtn {
      background-color: red;
    }

    .subnav-content {
      display: none;
      position: absolute;
      left: 0;
      background-color: red;
      width: 100%;
      z-index: 1;
    }

    .subnav-content a {
      float: left;
      color: white;
      text-decoration: none;
    }

    .subnav-content a:hover {
      background-color: #eee;
      color: black;
    }

    .subnav:hover .subnav-content {
      display: block;
    }
    </style>
    """
)

# HTML
st.write(
    """
    <div class="navbar">
      <a href="#home">Home</a>
      <div class="subnav">
        <button class="subnavbtn">01About <i class="fa fa-caret-down"></i></button>
        <div class="subnav-content">
          <a href="#company">Company</a>
          <a href="#team">Team</a>
          <a href="#careers">Careers</a>
        </div>
      </div>

      <div class="subnav">
        <button class="subnavbtn">02Services <i class="fa fa-caret-down"></i></button>
        <div class="subnav-content">
          <a href="#bring">Bring</a>
          <a href="#deliver">Deliver</a>
          <a href="#package">Package</a>
          <a href="#express">Express</a>
        </div>
      </div>

      <div class="subnav">
        <button class="subnavbtn">03Partners <i class="fa fa-caret-down"></i></button>
        <div class="subnav-content">
          <a href="#link1">Link 1</a>
          <a href="#link2">Link 2</a>
          <a href="#link3">Link 3</a>
          <a href="#link4">Link 4</a>
        </div>
      </div>
      <div class="subnav">
        <button class="subnavbtn">04Partners22 <i class="fa fa-caret-down"></i></button>
        <div class="subnav-content">
          <a href="#link1">Link 122</a>
          <a href="#link2">Link 222</a>
          <a href="#link3">Link 322</a>
          <a href="#link4">Link 224</a>
       </div>
  </div>
  <div class="subnav">
    <button class="subnavbtn">05ex <i class="fa fa-caret-down"></i></button>
    <div class="subnav-content">
      <a href="#link1">Link 1423</a>
      <a href="#link2">Link 1242</a>
      <a href="#link3">Link 143</a>
      <a href="#link4">Link 14</a>
    </div>
  </div>
   <div class="subnav">
    <button class="subnavbtn">06ww <i class="fa fa-caret-down"></i></button>
    <div class="subnav-content">
      <a href="#link1">Link 131c1</a>
      <a href="#link2">Link 1cc12</a>
      <a href="#link3">Link 1c3</a>
      <a href="#link4">Link 1c4</a>
    </div>
  </div>
  
</div>

<div style="padding:0 16px">
  <h1>PDF TOOLS</h1>
  <p>Welcome You</p>
</div>

</body>
</html>
 """
)