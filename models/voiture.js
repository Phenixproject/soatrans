import ServiceCRUD from "../services/crud";
import ClasseVoiture from "./classevoiture";
import Reservation from "./reservation";

export class Voiture{
    service_save = new ServiceCRUD();
    static service = new ServiceCRUD();

    selfReturn(){
        return new Voiture(this.id,this.numero_voiture,this.etat_voiture,this.classe)
    }

    setNumeroVoiture(numero_voiture){
        this.numero_voiture = numero_voiture;
        return this.selfReturn();
    }

    setEtatVoiture(etat_voiture){
        this.etat_voiture = etat_voiture;
        return this.selfReturn();
    }

    setClasse(classe){
        this.classe = classe;
        return this.selfReturn();
    }

    getData(){
        return {
            numero_voiture: this.numero_voiture,
            etat_voiture: this.etat_voiture,
            classe : this.classe.getData(),
        }
    }

    async save(){
        return await this.service_save.post("api/voitures/",this.getData());
    }

    async update(){
        return await this.service_save.put("api/voitures/",this.getData(),this.id);
    }

    async getInitReservation(){
        let reservation = await this.service_save.getSingle("client/initreservation/",this.id);
        console.log(reservation);
        return new Reservation(reservation.id,
            reservation.montant_paye,
            reservation.avance_paye,
            reservation.position_place,
            reservation.date,
            reservation.horaireclasse,
            reservation.utilisateur,
            reservation.voiture);
    }

    async getReservation(){
        let reservations = await this.service_save.getSingle("client/reservations/",this.id);
        let all_reservations = [];
        reservations.map(
            reservation => {
                let single_reservation = new Reservation(reservation.id,
                                            reservation.avance_paye,
                                            reservation.position_place,
                                            reservation.date,
                                            reservation.horaireclasse,
                                            reservation.utilisateur,
                                            reservation.voiture)
                all_reservations.push(single_reservation);
            }
        )
        return all_reservations;
    }

    static async rechercheVoiture(idhoraireclasse,date){
        let voiture = await this.service.post("client/creategetvoiture/",{"horaireclasse":idhoraireclasse,"date":date});
        return new Voiture(voiture.id,voiture.numero_voiture,voiture.etat_voiture,new ClasseVoiture(voiture.classe.id,voiture.classe.classe));
    }

    static async get(pk){
        let voiture = await this.service.getSingle("api/voitures/",pk);
        return new Voiture(voiture.id,voiture.numero_voiture,voiture.etat_voiture,voiture.classe);
    }

    static async getMany(){
        let voitures = await this.service.getMany("api/voitures/");
        let all_voitures = [];
        voitures.map(
            voiture => {
                let single_voiture = new Voiture(voiture.id,voiture.numero_voiture,voiture.etat_voiture,voiture.classe);
                all_voitures.push(single_voiture);
            }
        );
        return all_voitures;
    }

    constructor(id,numero_voiture,etat_voiture,classe=new ClasseVoiture()){
        this.id = id;
        this.numero_voiture = numero_voiture;
        this.etat_voiture = etat_voiture;
        this.classe = classe;
    }
}

export default Voiture;