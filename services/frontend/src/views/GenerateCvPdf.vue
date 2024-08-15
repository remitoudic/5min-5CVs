<template>
    <div>
        <h1>Generate and Display CV</h1>

        <form @submit.prevent="generateCV">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" v-model="cvData.name" required />
            </div>

            <div>
                <label for="career_objectives">Career Objectives:</label>
                <textarea id="career_objectives" v-model="cvData.career_objectives" required></textarea>
            </div>

            <div>
                <label for="work_experience">Work Experience:</label>
                <div v-for="(experience, index) in cvData.work_experience" :key="index">
                    <input type="text" placeholder="Position" v-model="experience.position" required />
                    <input type="text" placeholder="Company" v-model="experience.company" required />
                    <input type="text" placeholder="Date" v-model="experience.date" required />
                </div>
                <button type="button" @click="addWorkExperience">Add Work Experience</button>
            </div>

            <div>
                <label for="education">Education:</label>
                <div v-for="(edu, index) in cvData.education" :key="index">
                    <input type="text" placeholder="School" v-model="edu.school" required />
                    <input type="text" placeholder="Date" v-model="edu.date" required />
                </div>
                <button type="button" @click="addEducation">Add Education</button>
            </div>

            <button type="submit">Generate CV</button>
        </form>

        <div v-if="pdfUrl">
            <h2>Your CV PDF:</h2>
            <iframe :src="pdfUrl" width="100%" height="600px"></iframe>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cvData: {
                name: "",
                career_objectives: "",
                work_experience: [
                    { position: "", company: "", date: "" }
                ],
                education: [
                    { school: "", date: "" }
                ]
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
                const response = await fetch("http://127.0.0.1:8000/pdf", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.cvData)
                });
                console.log( JSON.stringify(this.cvData))
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

<style>
/* Add some basic styling */
form {
    margin-bottom: 20px;
}

input,
textarea {
    display: block;
    margin-bottom: 10px;
}

button {
    margin-top: 10px;
}

iframe {
    border: none;
}
</style>