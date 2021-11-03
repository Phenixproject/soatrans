import ServiceCRUD from "../services/crud";

export class Paiement{
    service_save = new ServiceCRUD();
    static service = new ServiceCRUD();

    selfReturn(){
        return new Paiement(this.id,this.date,
                this.montant,this.personnel,)
    }

    setDate(date){
        this.date = date;
        return this.selfReturn();
    }

    setMontant(montant){
        this.montant = montant;
        return this.selfReturn();
    }

    setPersonnel(personnel){
        this.personnel = personnel;
        return this.selfReturn();
    }

    setReservation(reservation){
        this.reservation = reservation;
        return this.selfReturn();
    }

    getData(){
        return {
            date: this.date,
            montant: this.montant,
            personnel: this.personnel.id,
            reservation: this.reservation,
        }
    }

    async save(){
        return await this.service_save.post("api/paiements/",this.getData());
    }

    async update(){
        return await this.service_save.update("api/paiements/",this.getData,this.id);
    }

    static async get(pk){
        let paiement = await this.service.getSingle("api/paiements/",pk);
        return new Paiement(paiement.id, 
            paiement.date,
            paiement.montant,
            paiement.personnel,
            paiement.reservation);
    }

    static async getMany(){
        let paiements = await this.service.getMany("api/paiements/");
        let all_paiements = []
        paiements.map(
            paiement => {
                let single_paiement = new Paiement(paiement.id,
                    paiement.date,
                    paiement.montant,
                    paiement.personnel,
                    paiement.reservation)
                all_paiements.push(paiement);
            }
        )
        return all_paiements;
    }

    static async getReservationAvancees(pk){
        let paiements = await this.service.getSingle("api/reservationsavancees/",pk);
        let all_paiements = []
        paiements.map(
            paiement => {
                let single_paiement = new Paiement(paiement.id,
                    paiement.date,
                    paiement.montant,
                    paiement.personnel,
                    paiement.reservation)
                all_paiements.push(paiement);
            }
        )
        return all_paiements;
    }


    static async getReservationPayer(pk){
        let paiements = await this.service.getSingle("api/reservationspayees/",pk);
        let all_paiements = []
        paiements.map(
            paiement => {
                let single_paiement = new Paiement(paiement.id,
                    paiement.date,
                    paiement.montant,
                    paiement.personnel,
                    paiement.reservation)
                all_paiements.push(paiement);
            }
        )
        return all_paiements;
    }

    constructor(id,date,montant,personnel,reservation){
        this.id = id;
        this.montant = montant;
        this.date = date;
        this.personnel = personnel;
        this.reservation = reservation;
    }
}

export default Paiement