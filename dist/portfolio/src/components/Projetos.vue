<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Projetos</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage" :type="alertType"></alert>
        <button
            type="button"  
            class="btn btn-success btn-sm"
            @click="toggleAddProjectModal">
            Adicionar Projetos
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Título</th>
              <th scope="col">Imagem</th>
              <th scope="col">Área</th>
              <th scope="col">Descrição</th>
              <th scope="col">Visivel?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(projeto, index) in projetos" :key="index">
                <td>{{ projeto.Título }}</td>
                <td>
                    <img :src="projeto.Imagem" :alt="projeto.Título" class="img-fluid" style="max-width: 100px; max-height: 100px;">
                </td>
                <td class="text-nowrap">{{ projeto.Área }} m²</td>
                <td>{{ projeto.Descrição }}</td>
                <td>
                    <span v-if="projeto.Visivel">Yes</span>
                    <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div
    ref="addProjectModal"
    class="modal fade"
    :class="{ show: activeAddProjectModal, 'd-block': activeAddProjectModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Add a new project</h5>
            <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleAddProjectModal">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <form>
                <div class="mb-3">
                    <label for="addProjectTitle" class="form-label">Título:</label>
                    <input
                    type="text"
                    class="form-control"
                    id="addProjectTitle"
                    v-model="addProjectForm.Título"
                    placeholder="Adicione Título">
                </div>
                <!-- <div class="mb-3">
                    <label for="addProjectImage" class="form-label">Imagem:</label>
                    <input
                    type="text" 
                    class="form-control"
                    id="addProjectImage"
                    v-model="addProjectForm.Imagem"
                    placeholder="Adicione Imagem">
                </div> -->
                <div class="mb-3">
                    <label for="addProjectImage" class="form-label">Imagem:</label>
                    <input
                        type="file"
                        class="form-control"
                        id="addProjectImage"
                        @change="handleImageUpload">
                </div>
                <div class="mb-3">
                    <label for="addProjectArea" class="form-label">Área:</label>
                    <input
                    type="number"
                    class="form-control"
                    id="addProjectArea"
                    v-model="addProjectForm.Área"
                    placeholder="Adicione Área">
                </div>
                <div class="mb-3">
                    <label for="addProjectDescription" class="form-label">Descrição:</label>
                    <input
                    type="text"
                    class="form-control"
                    id="addProjectDescription"
                    v-model="addProjectForm.Descrição"
                    placeholder="Adicione Descrição">
                </div>
                <div class="mb-3 form-check">
                    <input
                    type="checkbox"
                    class="form-check-input"
                    id="addProjectVisivel"
                    v-model="addProjectForm.Visivel">
                    <label class="form-check-label" for="addProjectVisivel">Visivel?</label>
                </div>
                <div class="btn-group" role="group">
                    <button
                    type="button"
                    class="btn btn-primary btn-sm"
                    @click="handleAddSubmit">
                    Submit
                    </button>
                    <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleAddReset">
                    Reset
                    </button>
                </div>
            </form>
        </div>
        </div>
    </div>
    </div>
    <div v-if="activeAddProjectModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
    data() {
        return {
            activeAddProjectModal: false,
            addProjectForm: {
                Título: '',
                Imagem: '',
                Área: 0,
                Descrição: '',
                Visivel: [],
            },
            projetos: [],
            message: '',
            showMessage: false,
            alertType: '',
            imageBasePath: '../assets/'
        }
    },
    components: {
        alert: Alert
    },
    methods: {
        addProject(payload) {
            const path = 'http://localhost:5001/projetos'
            axios.post(path, payload)
                .then(() => {
                    this.getProjects()
                    this.message = 'Projeto Adicionado!'
                    this.alertType = 'success'
                    this.showMessage = true
                    setTimeout(() => {
                        this.showMessage = false
                    }, 5000)
                })
                .catch((error) => {
                    console.log(error)
                    this.getProjects()
                    this.message = 'Erro ao adicionar projeto!'
                    this.alertType = 'danger'
                    this.showMessage = true
                    setTimeout(() => {
                        this.showMessage = false
                    }, 5000)
                })
        },
        getProjects() {
            const path = 'http://localhost:5001/projetos'
            axios.get(path)
                .then((res) => {
                    this.projetos = res.data.projetos
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        getImagePath(imageName) {
            return this.imageBasePath + imageName
        },
        handleAddReset() {
            this.initForm();
        },
        handleAddSubmit() {
            this.toggleAddProjectModal();
            let Visivel = false;
            if (this.addProjectForm.Visivel[0]) {
                Visivel = true
            }
            const payload = {
                Título: this.addProjectForm.Título,
                Imagem: this.addProjectForm.Imagem,
                Área: this.addProjectForm.Área,
                Descrição: this.addProjectForm.Descrição,
                Visivel,
            }
            this.addProject(payload)
            this.initForm()
        },
        handleImageUpload(event) {
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onload = (e) => {
                this.addProjectForm.Imagem = e.target.result; // This will store the base64 encoded image
            };
            reader.readAsDataURL(file);
        },
        initForm() {
            this.addProjectForm.Título = ''
            this.addProjectForm.Imagem = ''
            this.addProjectForm.Área = ''
            this.addProjectForm.Descrição = ''
            this.addProjectForm.Visivel = []
        },
        toggleAddProjectModal() {
            const body = document.querySelector('body')
            this.activeAddProjectModal = !this.activeAddProjectModal
            if (this.activeAddProjectModal) {
                body.classList.add('modal-open')
            } else {
                body.classList.remove('modal-open')
            }
        }
    },
    created() {
        this.getProjects()
    }
}
</script>

<style>

</style>