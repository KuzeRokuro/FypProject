<!-- create player forms -->
<template>
    <div class="container mb-3">
        <form action="">
            <div class="mb-3">
                <label for="" class="form-label">
                    Name
                </label>
                <input 
                    type="text" 
                    class="form-control"
                    v-model="Name"
                />
            </div>
            <div class="mb-3">
                <label for="" class="form-label">
                    Phone Number
                </label>
                <input 
                    type="text" 
                    class="form-control"
                    v-model="phoneNumber"
                />
            </div>
            <div class="mb-3">
                <button clea
                    class="btn btn-primary"
                    @click.prevent="playerCreated({name, phoneNumber})"
                >CREATE</button>
            </div>
        </form>
    </div>
</template>
<script>
export default {
    props: ['playerCreated'],
    data() {
        return {
            Name: '',
            phoneNumber: ''
        }
    }
}
</script>