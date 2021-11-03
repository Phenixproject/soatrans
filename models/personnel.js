import ServiceCRUD from "../services/crud";

export class Personnel{
    service_save = new ServiceCRUD();
    static service = new ServiceCRUD();

    selfReturn(){
        return new Personnel(this.id,this.username_personnel,
            this.first_name_personne,
            this.last_name_personnel,
            this.matricule_personnel,
            this.CIN_personnel,
            this.telephone_personnel,
            this.password_personnel,
            this.statut_personnel,
            this.local,
            this.role)
    }

    setUserName(username_personnel){
        this.username_personnel = username_personnel;
        return this.selfReturn();
    }

    setFirstName(first_name_personne){
        this.first_name_personne = first_name_personne;
        return this.selfReturn();
    }

    sefLastName(last_name_personnel){
        this.last_name_personnel = last_name_personnel;
        return this.selfReturn();
    }

    setMatriculePersonnel(matricule_personnel){
        this.matricule_personnel = matricule_personnel;
        return this.selfReturn();
    }

    setCIN(CIN_personnel){
        this.CIN_personnel = CIN_personnel;
        return this.selfReturn();
    }

    setTelephone(telephone_personnel){
        this.telephone_personnel = telephone_personnel;
        return this.selfReturn();
    }

    setPassword(password){
        this.password_personnel = password;
        return this.selfReturn();
    }

    setStatut(statut_personnel){
        this.statut_personnel = statut_personnel;
        return this.selfReturn();
    }

    setLocal(local){
        this.local = local;
        return this.selfReturn();
    }

    setRole(role){
        this.role = role;
        return this.selfReturn();
    }

    getData(){
        return {
            username_personnel : this.username_personnel,
            first_name_personne: this.first_name_personne,
            last_name_personnel:this.last_name_personnel,
            matricule_personnel: this.matricule_personnel,
            CIN_personnel: this.CIN_personnel,
            telephone_personnel: this.telephone_personnel,
            password_personnel: this.password_personnel,
            statut_personnel: this.statut_personnel,
            local:this.local.id,
            role:this.role.id,
        }
    }

    async save(){
        return await this.service_save.post("api/personnels/",this.getData());
    }

    async update(){
        return await this.service_save.put("api/personnels/",this.getData(),this.id);
    }

    static async get(pk){
        let personnel = await this.service.getSingle("api/personnels/",pk);
        return new Personnel(personnel.id,
                                personnel.username_personnel,
                                personnel.first_name_personne,
                                personnel.last_name_personnel,
                                personnel.matricule_personnel,
                                personnel.CIN_personnel,
                                personnel.telephone_personnel,
                                personnel.password_personnel,
                                personnel.statut_personnel,
                                personnel.local,
                                personnel.role);
    }

    static async getReservationUnpaid(pk){
        let personnels = await this.service.get("api/reservationsimpayees/",pk);
        let all_personnels = [];
        personnels.map(
            personnel => {
                let single_personnel = new Personnel(personnel.id,
                                        personnel.username_personnel,
                                        personnel.first_name_personne,
                                        personnel.last_name_personnel,
                                        personnel.matricule_personnel,
                                        personnel.CIN_personnel,
                                        personnel.telephone_personnel,
                                        personnel.password_personnel,
                                        personnel.statut_personnel,
                                        personnel.local,
                                        personnel.role)
                all_personnels.push(single_personnel);
            }
        )
        return all_personnels;
    }

    static async getMany(){
        let personnels = await this.service.getMany("api/personnels/");
        let all_personnels = [];
        personnels.map(
            personnel => {
                let single_personnel = new Personnel(personnel.id,
                                        personnel.username_personnel,
                                        personnel.first_name_personne,
                                        personnel.last_name_personnel,
                                        personnel.matricule_personnel,
                                        personnel.CIN_personnel,
                                        personnel.telephone_personnel,
                                        personnel.password_personnel,
                                        personnel.statut_personnel,
                                        personnel.local,
                                        personnel.role)
                all_personnels.push(single_personnel);
            }
        )
        return all_personnels;
    }

    constructor(id,username_personnel,
                first_name_personne,
                last_name_personnel,
                matricule_personnel,
                CIN_personnel,
                telephone_personnel,
                password_personnel,
                statut_personnel,
                local,
                role){
        this.id = id;
        this.username_personnel = username_personnel;
        this.first_name_personne = first_name_personne;
        this.last_name_personnel = last_name_personnel;
        this.matricule_personnel = matricule_personnel;
        this.CIN_personnel = CIN_personnel;
        this.telephone_personnel = telephone_personnel;
        this.password_personnel = password_personnel;
        this.statut_personnel = statut_personnel;
        this.local = local;
        this.role = role;
    }
}

export default Personnel