<template>
  <center>
  <div id="app">
    <router-view />
  </div>
  </center>
</template>

<style>

body {
    background-color: #dbdbdb;
}

#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width:600px;
  height:100%;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}


.btn-color {
  background-color: #1c4b99;
}

.card_alter{
  margin-top:20px;
  margin-bottom:0px;
  background-color: #dbdbdb; 
  border:0; 
}

.card_border {
  border:0;
  margin-bottom: 50px;
}

.card_mod {
  background-color: #f58384; 
  border:0; color: white; 
  margin-top: 20px; 
  margin-bottom: 10px;
}

.card_title_mod {
  font-size: 90px;
  font-family: Arial;
  font-weight: bold;
}

.card_header_mod {
  background-color: #f58384;
}

.card_title_todo_mod {
  font-size: 24px;
  font-family: Arial;
  font-weight: bold;
  color: white;
}

.check_mod {
  text-align: left;
  margin-bottom: 10px
}

.group_mod {
  margin-bottom: 10px;
}

.font_awesome_mod {
  color: white;
}
</style>