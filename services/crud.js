import axios from "axios";

export class ServiceCRUD{
    baseUrl = "http://127.0.0.1:8000/";
    
    async post(uri,data){
        return await axios.post(this.baseUrl+uri,data).then(
            response => {
                return response.data;
            }
        )
    }

    async getSingle(uri, pk){
        return await axios.get(this.baseUrl+uri+pk).then(
            response => {
                return response.data;
            }
        )
    }

    async getMany(uri){
        return await axios.get(this.baseUrl+uri).then(
            response => {
                return response.data;
            }
        )
    }

    async put(uri,data,pk){
        return await axios.put(this.baseUrl+uri+pk,data).then(
            response => {
                return response.data;
            }
        )
    }

    async putSpecial(uri,data){
        return await axios.put(this.baseUrl+uri,data).then(
            response => {
                return response;
            }
        )
    }

    delete(uri,pk){
        axios.delete(this.baseUrl+uri+pk).then(
            response => {
                console.log(response);
            }
        )
    }
}

export default ServiceCRUD