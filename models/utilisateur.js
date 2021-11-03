import ServiceCRUD from "../services/crud";

export class Client{
    baseUrl = "https://127.0.0.1:8000/api";
    service_save = new ServiceCRUD();
    static service = new ServiceCRUD();
    photo = ""

    ///////////////////////////instance d'une nouvelle classe/////////////////////////////

    selfReturn(){
        return new Client(this.id,this.username,this.last_name,
            this.first_name,this.CIN,
            this.telephone_utilisateur,
            this.statut_utilisateur,this.sexe,
            this.adresse, this.password, this.photo);
    }

    //////////////////////////fonction de modification des attributs de la classe/////////////////////////////

    setUserName(){
        this.username = this.first_name + " " + this.last_name;
        return this.selfReturn();
    }

    setLastName(lastname){
        this.last_name = lastname;
        this.setUserName();
        return this.selfReturn();
    }

    setFirstName(firstname){
        this.first_name = firstname;
        this.setUserName();
        return this.selfReturn();
    }

    setTelephone(telephone_utilisateur){
        this.telephone_utilisateur = telephone_utilisateur;
        return this.selfReturn();
    }

    setCIN(CIN){
        this.CIN = CIN;
        return this.selfReturn();
    }

    setStatutUtilisateur(statut){
        this.statut_utilisateur = statut;
        return this.selfReturn();
    }

    setSexe(sexe){
        this.sexe = sexe;
        return this.selfReturn();
    }

    setAdresse(adresse){
        this.adresse = adresse;
        return this.selfReturn();
    }

    setPassword(password){
        this.password = password;
        return this.selfReturn();
    }

    setPhoto(photo){
        this.photo = photo;
        return this.selfReturn();
    }

    ///////////////////////////modelisation des donnees a transferer vers l'api/////////////////////////////

    getDataWithoutPhoto(){
        return {
            id : this.id,
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name,
            CIN: this.CIN,
            telephone_utilisateur: this.telephone_utilisateur,
            statut_utilisateur: this.statut_utilisateur,
            adresse: this.adresse,
            sexe: this.sexe,
        }
    }

    getData(){
        return {
            id : this.id,
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name,
            CIN: this.CIN,
            telephone_utilisateur: this.telephone_utilisateur,
            statut_utilisateur: this.statut_utilisateur,
            adresse: this.adresse,
            sexe: this.sexe,
            photo: this.photo,
        }
    }

    getFormDataPhoto(){
        let formData = new FormData();
        formData.append('photo',this.photo,this.first_name+"_"+this.last_name+".jpg");
        return formData;
    }

    getFormData(){
        let formData = new FormData();
        formData.append('username',this.username);
        formData.append('last_name',this.last_name);
        formData.append('first_name', this.first_name);
        formData.append('CIN', this.CIN);
        formData.append('telephone_utilisateur', this.telephone_utilisateur);
        formData.append('sexe', this.sexe);
        formData.append('adresse', this.adresse);
        formData.append('statut_utilisateur', this.statut_utilisateur);
        formData.append('photo', this.photo, this.last_name+"_"+this.first_name+".jpg");
        return formData;
    }

    ///////////////////////////utilisation du serviceCRUD/////////////////////////////
        ///////////////sauvegarde des donnees////////////////////
    async save(){
        return await this.service_save.post("client/creationclients",this.getFormData());
    }

        ///////////////mise a jour des donnees///////////////////
    async update(){
        let customer = await this.service_save.put("client/",this.getDataWithoutPhoto(),this.id);
        if(this.photo.name)
            return await this.service_save.put("client/photo/",this.getFormDataPhoto(),this.id);
    }

        /////////////////////////methode static////////////////////////////////////
            //////////appel methode get pour obtenir un seul classe//////////////
    static async get(pk){
        let customer = await this.service.getSingle("client/",pk);
        let cust = new Client(customer.id,customer.username,customer.last_name,
            customer.first_name,customer.CIN,
            customer.telephone_utilisateur,
            customer.statut_utilisateur,customer.sexe,
            customer.adresse, customer.password, customer.photo)
        return cust;
    }

            //////////appel methode get pour obtenir tous les classes////////////
    static async getMany(){
        let customers = await this.service.getMany("client/");
        let all_customers = [];
        customers.map(
            customer => {
                let cust = new Client(customer.id,customer.username,customer.last_name,
                    customer.first_name,customer.CIN,
                    customer.telephone_utilisateur,
                    customer.statut_utilisateur,customer.sexe,
                    customer.adresse, customer.password, customer.photo);
                all_customers.push(cust);
            }
        )
        return all_customers;
    }

            //////////effacer la classe///////////////////////////////////////////////////////
    static async deleteClient(pk){
        await this.service.delete("client/",pk)
    }

    ///////////////////////////constructeur classe/////////////////////////////

    constructor(id,username,last_name,
                first_name,CIN,
                telephone_utilisateur,
                statut_utilisateur=false,sexe,
                adresse, password, photo=""){
        this.id = id;
        this.username = username;
        this.last_name = last_name;
        this.first_name = first_name;
        this.CIN = CIN;
        this.sexe = sexe;
        this.telephone_utilisateur = telephone_utilisateur;
        this.statut_utilisateur = statut_utilisateur;
        this.photo = photo;
        this.adresse = adresse;
        this.password = password;
    }
}

export default Client;