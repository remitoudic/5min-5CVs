<template>
  <div id="home-view">
    <Navbar />
    <div class="content">
      <h1 class="title">CV Builder</h1>

      <tabs>
        <tab title="Manual Form">
          <!-- Form for generating CV -->
          <form @submit.prevent="generateCV" class="cv-form">
            <div class="form-group">
              <label for="name">Name:</label>
              <input type="text" id="name" v-model="cvData.name" required />
            </div>

            <div class="form-group">
              <label for="career_objectives">Career Objectives:</label>
              <textarea id="career_objectives" v-model="cvData.career_objectives" required></textarea>
            </div>

            <div class="form-group">
              <label>Work Experience:</label>
              <div v-for="(experience, index) in cvData.work_experience" :key="index" class="experience-group">
                <input type="text" placeholder="Position" v-model="experience.position" required />
                <input type="text" placeholder="Company" v-model="experience.company" required />
                <input type="text" placeholder="Date" v-model="experience.date" required />
              </div>
              <button type="button" @click="addWorkExperience" class="add-btn">Add Work Experience</button>
            </div>

            <div class="form-group">
              <label>Education:</label>
              <div v-for="(edu, index) in cvData.education" :key="index" class="education-group">
                <input type="text" placeholder="School" v-model="edu.school" required />
                <input type="text" placeholder="Date" v-model="edu.date" required />
              </div>
              <button type="button" @click="addEducation" class="add-btn">Add Education</button>
            </div>

            <button type="submit" class="submit-btn">Generate CV</button>
          </form>
        </tab>
        <tab title="Load CV"> 
          <div class="load-cv-container">
            <h2>Load your CV</h2>
            <input type="file" @change="handleFileUpload" accept=".pdf" ref="fileInput" />
            <button @click="loadCV" class="load-btn" :disabled="!selectedFile">Load CV</button>
            <p v-if="loadMessage" :class="{'success-message': loadSuccess, 'error-message': !loadSuccess}">
              {{ loadMessage }}
            </p>
          </div>
        </tab>
        <tab title="Load from LinkedIN">Load your data from LinkedIn feature</tab>
      </tabs>

      <!-- Display the generated PDF -->
      <div v-if="pdfUrl" class="pdf-container">
        <h2>Your CV PDF:</h2>
        <iframe :src="pdfUrl" width="100%" height="600px"></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import Tab from '../components/Tab.vue'
import Tabs from '../components/Tabs.vue'

export default {
  name: 'HomeView',
  components: {
    Tab,
    Tabs
  },

  data() {
    return {
      cvData: {
        name: "",
        career_objectives: "",
        work_experience: [],
        education: []
      },
      pdfUrl: null,
      selectedFile: null,
      loadMessage: '',
      loadSuccess: false
    };
  },
  methods: {
    addWorkExperience() {
      this.cvData.work_experience.push({ position: "", company: "", date: "" });
    },
    addEducation() {
      this.cvData.education.push({ school: "", date: "" });
    },
    async generateCV() {
      try {
        const response = await fetch('http://0.0.0.0:8000/pdf', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.cvData)
        });

        if (!response.ok) {
          throw new Error("Failed to generate CV");
        }

        const blob = await response.blob();
        this.pdfUrl = URL.createObjectURL(blob);
      } catch (error) {
        console.error(error);
        alert("There was an error generating the CV.");
      }
    },
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    async loadCV() {
      if (!this.selectedFile) {
        this.loadMessage = 'Please select a file first.';
        this.loadSuccess = false;
        return;
      }

      const formData = new FormData();
      formData.append('file', this.selectedFile);

      try {
        const response = await fetch('http://0.0.0.0:8000/upload-cv', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          throw new Error("Failed to upload CV");
        }

        const result = await response.json();
        this.loadMessage = 'CV uploaded successfully!';
        this.loadSuccess = true;
        console.log(result); // You can handle the server response here
      } catch (error) {
        console.error(error);
        this.loadMessage = 'There was an error uploading the CV.';
        this.loadSuccess = false;
      }
    }
  }
};
</script>

<style scoped>
/* Existing styles... */

.load-cv-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.load-btn {
  background-color: #66bb6a;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}

.load-btn:hover {
  background-color: #4caf50;
}

.load-btn:disabled {
  background-color: #c8e6c9;
  cursor: not-allowed;
}

.success-message {
  color: #2e7d32;
}

.error-message {
  color: #c62828;
}
</style>
