<template>
    <div>
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
          <a href="#home"><img id="home" src="/logo.png" alt="logo" class="navbar-brand img-fluid"></a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse topp" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <router-link to="/" class="nav-link" aria-current="page">
                  Home
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/projetos" class="nav-link">Projetos</router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about">Sobre</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#contact">Contato</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
      <!-- Hero Section -->
      <section class="hero-section bg-dark text-white text-center d-flex align-items-center justify-content-center">
        <div class="container">
          <h1 class="display-4">Escritório de Arquitetura em Tramandaí</h1>
          <a href="#services" class="btn btn-outline-light btn-lg mt-3">Nossos Serviços</a>
        </div>
      </section>
  
<!-- Services Section -->
<section id="services" class="py-5">
  <div class="container">
    <h2 class="text-center">Nossos Serviços</h2>
    <div class="row">
      <!-- Dynamically list only visible projects -->
      <div
        v-for="(projeto, index) in projetos.filter(projeto => projeto.Visivel)"
        :key="index"
        class="col-md-4 mb-4"
      >
        <div class="card h-100 text-center">
          <img
            :src="projeto.Imagem"
            :alt="projeto.Título"
            class="card-img-top"
            style="max-height: 200px; object-fit: cover;"
          />
          <div class="card-body">
            <h5 class="card-title">{{ projeto.Título }}</h5>
            <p class="card-text">{{ projeto.Descrição }}</p>
            <p><strong>Área:</strong> {{ projeto.Área }} m²</p>
            <a href="#" class="btn btn-primary">Ver Mais</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

  
    <!-- About Section -->
    <section id="about" class="py-5">
      <div class="container">
        <div class="row align-items-center">
          <!-- Column for the image -->
          <div class="col-md-6 text-center mb-4 mb-md-0">
            <img src="/profile.jpeg" alt="About Image" class="img-fluid about-image">
          </div>

          <!-- Column for the text -->
          <div class="col-md-6">
            <h2>Sobre Nós</h2>
            <p class="lead">
              Somos uma empresa de arquitetura focada em criar espaços que 
              unem beleza, funcionalidade e sustentabilidade.
            </p>
            <p>
              Com uma equipe de profissionais experientes, oferecemos projetos 
              inovadores e personalizados que atendem às necessidades dos nossos clientes.
            </p>
          </div>
        </div>
      </div>
    </section>


  
      <!-- Contact Section -->
      <section id="contact" class="py-5">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-6">
              <h2 class="text-center">Fale Conosco</h2>
              <form>
                <div class="mb-3">
                  <label for="name" class="form-label">Nome</label>
                  <input type="text" class="form-control" id="name" placeholder="Seu nome">
                </div>
                <div class="mb-3">
                  <label for="email" class="form-label">Email</label>
                  <input type="email" class="form-control" id="email" placeholder="Seu email">
                </div>
                <div class="mb-3">
                  <label for="message" class="form-label">Mensagem</label>
                  <textarea class="form-control" id="message" rows="4" placeholder="Sua mensagem"></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">Enviar</button>
              </form>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Footer -->
      <footer class="text-center py-3">
        <div class="container">
          <p class="mb-0">&copy; 2024 Willian Oliveira Arquitetura. Todos os direitos reservados.</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        projetos: []
      };
    },
    methods: {
      getProjects() {
        const path = 'http://localhost:5001/projetos';
        axios.get(path)
          .then((res) => {
            this.projetos = res.data.projetos;
          })
          .catch((error) => {
            console.error('Erro ao carregar os projetos:', error);
          });
      }
    },
    created() {
      this.getProjects();
    }
  };


  document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.querySelector('.navbar-toggler');
  toggleButton.addEventListener('click', () => {
    console.log('Navbar toggler clicked');
  });
});

  </script>
  
  <style scoped>  

footer,
#about {
  background-color: #1d3c34;
  color: #9a7f61;
}

#navbarNav {
  background-color: #22463d;
  color: #9a7f61;
  padding: 5px;
  width: 100%;
  border: 5px solid #1d3c34;
}

.card img {
  height: 200px;
  object-fit: cover;
}

/* Navbar */
.navbar {
  background-color: #1d3c34;
  height: 70px; /* Explicit height for the navbar */
  position: fixed; /* Fix the navbar position */
  top: 0; /* Align to the top */
  width: 100%; /* Full width */
  z-index: 1000; /* High z-index to be on top */
}

/* Hero Section */
.hero-section {
  padding-top: 70px; /* Make space for the fixed navbar */
  min-height: calc(100vh - 70px); /* Ensure it occupies the full height */
  background: url('/hero.jpeg') center/cover no-repeat;
  color: white;
  position: relative;
  z-index: 1; /* Ensure it's below the navbar */
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Dark overlay */
  z-index: 1; /* Ensure overlay is above the background image */
}

.hero-section .container {
  position: relative;
  z-index: 2; /* Content on top of the overlay */
}

.navbar img {
  max-height: 60px;
}

.navbar a {
  color: #9a7f61;
}

.about-image {
  max-height: 500px;
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Stronger shadow for more depth */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effect */
}

/* Hover effect */
.about-image:hover {
  transform: scale(1.05); /* Slightly enlarge the image on hover */
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3); /* Increase shadow on hover */
}

#services,
#contact {
  background-color: #e5e1e6;
}

  </style>
  