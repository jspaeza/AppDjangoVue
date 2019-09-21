<template>
    <div>
        <div>
            <label>File Preview
                <input type="file" id="file" ref="file" accept="image/*" v-on:change="handleFileUpload()"/>
            </label>
            <img v-bind:src="imagePreview" v-show="showPreview"/>
        </div>
        <div>
            <button v-on:click="submitFiles()">Submit</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                file: '',
                showPreview: false,
                imagePreview: ''
            }
        },

        methods: {
            submitFiles() {
                let formData = new FormData();
                formData.append("title", "Prueba");
                formData.append("sinopsis", "Esto es una prueba");
                formData.append("imagen", this.file);

                axios.post( 'http://localhost:8000/',
                    formData,
                    {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                    }
                ).then(function() {
                    console.log('SUCCESS!!');
                })
                .catch(function() {
                    console.log('FAILURE!!');
                });
            },

            handleFileUpload() {
        
                this.file = this.$refs.file.files[0];

                let reader  = new FileReader();

                reader.addEventListener("load", function () {
                    this.showPreview = true;
                    this.imagePreview = reader.result;
                    }.bind(this), false);

                if(this.file) {
                    if (/\.(jpe?g|png|gif)$/i.test( this.file.name )) {
                        reader.readAsDataURL(this.file);
                    }
                }
            }
        }   
    }
</script>

<style>
  input[type="file"] {
    position: absolute;
    top: -500px;
    max-width: 30%;
  }
  div.file-listing img {
    max-width: 90%;
  }
</style>