<template>
  <div class="cv-preview">
    <div class="header">
      <h2>{{ cvData.name }}</h2>
      <p>{{ cvData.email }}</p>
    </div>

    <div class="section">
      <h3>Career Objective</h3>
      <p>{{ cvData.objective }}</p>
    </div>

    <div class="section">
      <h3>Work Experience</h3>
      <ul>
        <li v-for="(job, index) in cvData.experience" :key="index">
          <strong>{{ job.title }}</strong> at <strong>{{ job.company }}</strong>
          <span class="years">({{ job.years }})</span>
          <p class="job-description">{{ job.description }}</p>
        </li>
      </ul>
    </div>

    <div class="section">
      <h3>Education</h3>
      <ul>
        <li v-for="(edu, index) in cvData.education" :key="index">
          <strong>{{ edu.degree }}</strong> from <strong>{{ edu.institution }}</strong>
          <span class="years">({{ edu.year }})</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CvT',
  props: {
    cvData: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.cv-preview {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #e0f7e0; /* Light green background */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

.header h2 {
  font-size: 2rem;
  margin-bottom: 5px;
}

.header p {
  font-size: 1rem;
  color: #666;
}

.section {
  margin-bottom: 20px;
}

.section h3 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 10px;
  border-bottom: 2px solid #333;
  padding-bottom: 5px;
}

.section ul {
  list-style-type: none;
  padding: 0;
}

.section ul li {
  margin-bottom: 15px;
}

.years {
  font-style: italic;
  color: #666;
  margin-left: 10px;
}

.job-description {
  margin-top: 5px;
  color: #555;
}
</style>
