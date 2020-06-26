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


            <form  id="createCarteirinha"  @submit.prevent="handleSubmit">
             <div class="row">
               <div id="msg_sucess" class="col-sm-12" style="margin-bottom:20px;display:none;">
                    <a class="button" v-on:click="Download()">Download do Documento</a>
               </div>
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
                       <button class="form-control" v-on:click="handleSubmit()">Enviar Dados</button>
                  </div>
             </div>
           </form>
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
                    avatar: "",
                    carteirinha: ""
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
               this.user.avatar = event.target.files[0]
            },
            handleSubmit() {
                this.submitted = true;

                // stop here if form is invalid
                this.$v.$touch();
                if (this.$v.$invalid) {
                    return;
                }
                console.log(this.user.avatar)
                let payload = new FormData();
                payload.append('username', this.user.username);
                payload.append('psn', this.user.psn);
                payload.append('nintendo', this.user.nintendo);
                payload.append('xbox', this.user.xbox);
                payload.append('steam', this.user.steam);
                payload.append('otherdatas', this.user.otherdatas);
                payload.append('avatar', this.user.avatar);

                const path = "http://localhost:5000/carteirinha";
                axios
                  .post(path,payload,{
                   headers: {
                      'Content-Type': 'multipart/form-data'
                    }

                    }).then((msg) => {
                      if (msg.data.status =='success'){

                        var msg_sucess = document.getElementById("msg_sucess");
                        // Altera a div que vai aparecer
                        msg_sucess.style.display = "";
                        // Adiciona o caminho a carteirinha
                        this.user.carteirinha = msg.data.path
                      }
                    })
                      .catch(error => {
                      console.log(error);
                    });

            },
            Download() {
                console.log("entrou")
                this.submitted = false;

                var payload = this.user.carteirinha

                const path = "http://localhost:5000/uploads/"+ payload;
                axios
                  .post(path,payload,{
                   headers: {
                    }

                    }).then((response) => {

                       var fileURL = window.URL.createObjectURL(new Blob([response.data]));
                       var fileLink = document.createElement('a');

                       fileLink.href = fileURL;
                       fileLink.setAttribute('download', 'file.png');
                       document.body.appendChild(fileLink);

                       fileLink.click();
                    })
                      .catch(error => {
                      console.log(error);
                    });

            }
        },

    };



</script>
