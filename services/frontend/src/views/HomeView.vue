<template>
  <div id="home-view">
    <Navbar />
    <div class="content">
      <h1 class="title">CV Builder</h1>

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

      <!-- Display the generated PDF -->
      <div v-if="pdfUrl" class="pdf-container">
        <h2>Your CV PDF:</h2>
        <iframe :src="pdfUrl" width="100%" height="600px"></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      cvData: {
        name: "",
        career_objectives: "",
        work_experience: [],
        education: []
      },
      pdfUrl: null
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
    }
  }
};
</script>

<style scoped>
/* Styling for larger screens */
#home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1000px;
  min-height: 100vh;
  background-color: #e5f5e0; /* Light green background */
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

.content {
  background-color: white;
  padding: 30px; /* Increased padding for more spacious content */
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 1200px; /* Increased max-width for wider content */
  width: 100%;
  margin-top: 20px;
}

.title {
  font-size: 3rem; /* Larger font size for the title */
  margin-bottom: 20px;
  color: #2e7d32; /* Dark green color */
  text-align: center;
}

.cv-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-weight: bold;
  color: #388e3c; /* Green color */
  margin-bottom: 8px;
}

.form-group input,
.form-group textarea {
  padding: 12px; /* Increased padding for inputs and textarea */
  border: 1px solid #c8e6c9; /* Light green border */
  border-radius: 6px;
  font-size: 1.1rem; /* Larger font size for better readability */
}

.experience-group,
.education-group {
  display: flex;
  gap: 15px; /* Increased gap between fields */
  margin-bottom: 15px; /* Increased margin-bottom for spacing */
}

.add-btn,
.submit-btn {
  background-color: #66bb6a; /* Green button background */
  color: white;
  border: none;
  padding: 12px 20px; /* Increased padding for larger buttons */
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1rem; /* Larger font size for buttons */
  transition: background-color 0.3s ease;
}

.add-btn:hover,
.submit-btn:hover {
  background-color: #4caf50; /* Darker green on hover */
}

.pdf-container {
  margin-top: 40px;
}

.pdf-container h2 {
  color: #2e7d32; /* Dark green color */
  margin-bottom: 20px;
}

iframe {
  border: 2px solid #c8e6c9; /* Light green border for iframe */
  border-radius: 6px;
}
</style>

