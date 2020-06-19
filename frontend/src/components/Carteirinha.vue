<template>

<div class="container">
  <div class="row">
    <div class="col-sm-12">
        <div class="card card_alter">
          <div class="card-body">
            <h1 class="card-title card_title_mod"><img src="/logo.png"> </h1>
          </div>
        </div>
    </div>
  </div>
  
      <div class="card card_border">
        <div class="card-header card_header_mod">
            <h3 class="card-title card_title_todo_mod">Crie o Seu Documento Gamer</h3>
        </div>
        <div class="card-body">
          <div class="input-group mb-3 group_mod">
            <form  id="createCarteirinha"  @submit.prevent="handleSubmit">
             <div class="row">
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="username">Nickname: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <input id="username" v-model="user.username" type="text" name="username" class="form-control" placeholder="Como é conhecido nos jogos..." aria-describedby="basic-addon1">
                  </div>    
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="psn">PSN ID: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <input id="psn" v-model="user.psn"  type="text" name="psn" class="form-control" placeholder="Sua PSN.." aria-describedby="basic-addon1">
                  </div>  
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="nintendo">Friend CODE: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <input id="nintendo" v-model="user.nintendo"  type="text" class="form-control" name="nintendo" placeholder="Seu Friend Code..." aria-describedby="basic-addon1">
                  </div>  
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="xbox">TAG Gamer: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <input id="xbox" v-model="user.xbox" type="text" name="xbox" class="form-control" placeholder="Seu TAG Gamer..." aria-label="Comprar" aria-describedby="basic-addon1">
                  </div>  
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="steam">Steam: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <input id="steam" v-model="user.steam" type="text" name="steam" class="form-control" placeholder="Sua Steam..." aria-describedby="basic-addon1">
                  </div>  
                  <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="otherdatas">Dados Adicionais: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                      <textarea id="otherdatas" v-model="user.otherdatas" rows="4" name="otherdatas" placeholder="Outros dados que considera importante..." 
                      class="form-control"> </textarea>
                  </div>  
                   <div class="col-sm-4" style="margin-bottom:20px;">
                      <label for="file-photo">Foto: </label>
                  </div>
                  <div class="col-sm-8" style="margin-bottom:20px;">
                     <input type="file" accept="image/*"  name="avatar" v-on:change="uploadFile" class="form-control"  id="avatar">
                  </div>  
                   <div class="col-sm-8" style="margin-bottom:20px;">
                  </div>
                  <div class="col-sm-4" style="margin-bottom:20px;">
                       <button class="form-control" v-on:click="handleSubmit()">Enviar Dados</button>>
                  </div>  
             </div>
           </form>
        </div>
      </div>
    </div>
    </div>

 </template>

<script>
import axios from "axios";
import { required} from "vuelidate/lib/validators";
export default {
        name: "app",
        data() {
            return {
                user: {
                    username: "",
                    psn: "",
                    nintendo: "",
                    xbox: "",
                    otherdatas: "",
                    avatar: ""
                },
                submitted: false
            };
        },
        validations: {
            user: {
                username: { required }
            }
        },
        methods: {
            uploadFile(event){
               console.log(event)
               this.user.avatar = event.target
               console.log(this.user.avatar)
               alert(this.user.avatar);
            },
            handleSubmit() {
                this.submitted = true;

                // stop here if form is invalid
                this.$v.$touch();
                if (this.$v.$invalid) {
                    return;
                }
                //alert(this.user.avatar.value())
                const payload = {
                  username: this.user.username,
                  psn: this.user.psn,
                  nintendo: this.user.nintendo || "-",
                  xbox: this.user.xbox || "-",
                  steam: this.user.steam || "-",
                  otherdatas: this.user.therdatas || "-",
                  avatar: this.user.avatar || "icon.png"

                }; 
                
                const path = "http://localhost:5000/carteirinha";
                axios
                  .post(path,payload,{
                     headers: {
                        // remove headers
                      }
                    }).then(() => {
                      alert("funcionou")
                      //this.getJogos();
                    })
                      .catch(error => {
                      console.log(error);
                      //this.getJogos();
                    });

            }
        }
    };


</script>

