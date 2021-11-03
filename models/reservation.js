import ServiceCRUD from "../services/crud";
import Horaire from "./horaire";
import Personnel from "./personnel";
import Client from "./utilisateur";
import Voiture from "./voiture";

export class Reservation{
    service_save = new ServiceCRUD();
    static service = new ServiceCRUD();

    selfReturn(){
        return new Reservation(
            this.id,this.avance_paye,
            this.position_place,this.date,
            this.utilisateur,this.voiture
        )
    }

    setAvancePaye(avance_paye){
        this.avance_paye = avance_paye;
        return this.selfReturn();
    }

    setPositionPlace(position_place){
        this.position_place = position_place;
        return this.selfReturn();
    }

    setDate(date){
        this.date = date;
        return this.date;
    }

    setUtilisateur(utilisateur){
        this.utilisateur = utilisateur;
        return this.selfReturn();
    }

    setVoiture(voiture){
        this.voiture = voiture;
        return this.selfReturn();
    }

    setHoraireClasse(horaireclasse){
        this.horaireclasse = horaireclasse;
        return this.selfReturn();
    }

    getData(){
        return {
            id : this.id,
            avance_paye: this.avance_paye,
            date: this.date,
            utilisateur : this.utilisateur.id,
            voiture: this.voiture.id,
            horaireclasse: this.horaireclasse,
        }
    }

    async save(){
        return await this.service_save.post("api/reservations/",this.getData);
    }
    async update(){
        return await this.service_save.put("api/reservations/",this.getData(),this.id);
    }

    static async get(pk){
        let reservation = await this.service.getSingle("api/reservations/",pk);
        return new Reservation(reservation.id,
                    reservation.avance_paye,
                    reservation.position_place,
                    reservation.date,
                    reservation.horaireclasse,
                    reservation.utilisateur,
                    reservation.voiture);
    }

    static async getMany(){
        let reservations = await this.service_save.getMany("api/reservations/");
        let all_reservations = []
        reservations.map(
            reservation => {
                let single_reservation = new Reservation(reservation.id,
                    reservation.avance_paye,
                    reservation.position_place,
                    reservation.date,
                    reservation.horaireclasse,
                    reservation.utilisateur,
                    reservation.voiture);
                all_reservations.push(single_reservation);
            }
        )
        return all_reservations;
    }

    static async getReservationUnpaid(){
        let reservations = await this.service.getMany("api/reservationsimpayees/");
        let all_reservations = []
        reservations.map(
            reservation => {
                let single_reservation = new Reservation(reservation.id,
                    reservation.avance_paye,
                    reservation.position_place,
                    reservation.date,
                    reservation.horaireclasse,
                    reservation.utilisateur,
                    reservation.voiture);
                all_reservations.push(single_reservation);
            }
        )
        return all_reservations;
    }

    constructor(id,avance_paye,
                position_place,date,
                horaireclasse,
                utilisateur = new Client(),
                voiture = new Voiture()){
        this.id = id;
        this.avance_paye = avance_paye;
        this.position_place = position_place;
        this.date = date;
        this.horaireclasse = horaireclasse;
        this.utilisateur = utilisateur;
        this.voiture = voiture;
    }
}

export default Reservation