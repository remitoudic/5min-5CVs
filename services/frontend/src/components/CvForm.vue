<!-- components/CvForm.vue -->
<template>
    <form @submit.prevent="submitForm">
      <div>
        <h2>Personal Information</h2>
        <input v-model="form.name" placeholder="Full Name" required>
        <input v-model="form.email" type="email" placeholder="Email" required>
      </div>
  
      <div>
        <h2>Career Objective</h2>
        <textarea v-model="form.objective" placeholder="Career Objective" required></textarea>
      </div>
  
      <div>
        <h2>Work Experience</h2>
        <div v-for="(job, index) in form.experience" :key="index">
          <input v-model="job.title" placeholder="Job Title" required>
          <input v-model="job.company" placeholder="Company" required>
          <input v-model="job.years" placeholder="Years" required>
        </div>
        <button type="button" @click="addExperience">Add Experience</button>
      </div>
  
      <div>
        <h2>Education</h2>
        <div v-for="(edu, index) in form.education" :key="index">
          <input v-model="edu.degree" placeholder="Degree" required>
          <input v-model="edu.institution" placeholder="Institution" required>
          <input v-model="edu.year" placeholder="Year" required>
        </div>
        <button type="button" @click="addEducation">Add Education</button>
      </div>
  
      <button type="submit">Generate CV</button>
    </form>
  </template>
  
  <script>
  export default {
    name: 'CvForm',
    data() {
      return {
        form: {
          name: '',
          email: '',
          objective: '',
          experience: [{ title: '', company: '', years: '' }],
          education: [{ degree: '', institution: '', year: '' }]
        }
      };
    },
    methods: {
      addExperience() {
        this.form.experience.push({ title: '', company: '', years: '' });
      },
      addEducation() {
        this.form.education.push({ degree: '', institution: '', year: '' });
      },
      submitForm() {
        this.$emit('submit-cv', { ...this.form });
      }
    }
  };
  </script>
  
  