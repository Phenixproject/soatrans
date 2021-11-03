import React,{useState,useEffect} from "react";
import Destination from "../../models/destination";
import Horaire from "../../models/horaire";
import HoraireClasse from "../../models/horaireclasse";
import Paiement from "../../models/paiement";
import Personnel from "../../models/personnel";
import Reservation from "../../models/reservation";
import Client from "../../models/utilisateur";
import Voiture from "../../models/voiture";

function Formulaire(){
    const id = 5
    const id_horaire = 4
    const [client,setClient] = useState(new Client())
    const [horaire,setHoraire] = useState(new Horaire())
    const [horaires,setHoraires] = useState([])
    const [destination, setDestination] = useState(new Destination())
    const [destinations, setDestinations] = useState([])
    const [horaireclasse, setHoraireClasse] = useState(new HoraireClasse())
    const [horaireclasses, setHoraireClasses] = useState([])
    const [voiture,setVoiture] = useState(new Voiture());
    const [date,setDate] = useState("")
    const [paiement,setPaiement] = useState(new Paiement())
    const [personnel,setPersonnel] = useState(new Personnel())

    useEffect(async ()=>{
        setClient(await Client.get(id));
        setHoraire(await Horaire.get(id_horaire));
        setHoraires(await HoraireClasse.getHoraire(3));
        setDestination(await Destination.get(5));
        setDestinations(await HoraireClasse.getDestination(1));
        setVoiture(await Voiture.get(31));
        console.log(await Paiement.getMany());
        console.log(await Personnel.get(1));
        console.log(await Reservation.getReservationUnpaid());
        console.log(await Paiement.getReservationPayer(1));
        console.log(await Paiement.getReservationAvancees(1));
        setPaiement(await Paiement.get(1))
        //console.log(await HoraireClasse.getDestination(2));
        //console.log(await HoraireClasse.getHoraire(2));
    },[id,id_horaire])

    let handlerSubmit = async (e) => {
        e.preventDefault();
        console.log(await client.update());
    }

    let handlerHoraireSubmit = async (e) => {
        e.preventDefault();
        console.log(await horaire.update());
    }

    let handlerDestinationSubmit = async (e) => {
        e.preventDefault();
        console.log(await voiture.getReservation());
        //console.log(await destination.save())
    }

    let handlerVoiture = async (e) => {
        console.log(await Voiture.rechercheVoiture(8,date));
    }

    let showSomme = async () => {
        console.log(paiement.personnel);
    }

    const afficherImage = () => {
        console.log(client.photo.type);
        if(!client.photo.name)
            return (
                <div>
                    <img src={"http://127.0.0.1:8000"+client.photo} title={"http://127.0.0.1:8000"+client.photo}/>
                </div>
            )
        else{
            console.log(client.photo);
            let reader = new FileReader()
            let url_image = ""
            reader.readAsDataURL(client.photo);
            reader.onload = (_event) => {
                url_image = reader.result.toString();
            }
            console.log(url_image);
            return (
                <div>
                    <img src={url_image} title={url_image}/>
                </div>
            )
        }
    }

    return (
        <div>
            <form onSubmit={(e)=>{handlerSubmit(e)}}>
                <label>Nom : {client.first_name}</label>
                <input type="text" value={client.first_name} onChange={(e)=>{setClient(client.setFirstName(e.target.value))}}/>
                <label>Prenom(s) : {client.last_name}</label>
                <input type="text" value={client.last_name} onChange={(e)=>{setClient(client.setLastName(e.target.value))}}/>
                <label>Adresse : {client.adresse}</label>
                <input type="text" value={client.adresse} onChange={(e)=>{setClient(client.setAdresse(e.target.value))}}/>
                <label>Carte d'identite nationale : {client.CIN}</label>
                <input type="text" value={client.CIN} onChange={(e)=>{setClient(client.setCIN(e.target.value))}}/>
                <label>Numero de telephone : {client.telephone_utilisateur}</label>
                <input type="text" value={client.telephone_utilisateur} onChange={(e)=>{setClient(client.setTelephone(e.target.value))}}/>
                <label>Handicap : {client.handicap}</label>
                <input type="radio" name="handicap" value={client.handicap} onChange={(e)=>{setClient(client.setHandicap(false))}}/>
                <input type="radio" name="handicap" value={client.handicap} onChange={(e)=>{setClient(client.setHandicap(true))}}/>
                <label>Mot de passe : {client.password}</label>
                <input type="password" value={client.password} onChange={(e)=>{setClient(client.setPassword(e.target.value))}}/>
                <label>Photo</label>
                <input type="file" onChange={(e)=>{setClient(client.setPhoto(e.target.files[0]))}}/>
                <button>S'inscrire</button>
            </form>
            <form onSubmit={(e)=>{handlerHoraireSubmit(e)}}>
                <label>Heure: {horaire.heure}</label>
                <input type="text" value={horaire.heure} onChange={(e)=>{setHoraire(horaire.setHeure(e.target.value))}}/>
                <button>Submit</button>
            </form>
            <div>
            {
                horaires.map(
                    data => {
                        return (
                            <p>{data.heure}</p>
                        )
                    }
                )
            }
            </div>
            <form onSubmit={(e)=>{handlerDestinationSubmit(e)}}>
                <label>Depart: {destination.depart}</label>
                <input type="text" value={destination.depart} onChange={(e)=>{setDestination(destination.setDepart(e.target.value))}}/>
                <label>Depart: {destination.arrive}</label>
                <input type="text" value={destination.arrive} onChange={(e)=>{setDestination(destination.setArrive(e.target.value))}}/>
                <button>Submit</button>
            </form>
            <div>
            {
                destinations.map(
                    data => {
                        return (
                            <p>{data.depart}</p>
                        )
                    }
                )
            }
            </div>
            <p>{voiture.classe.classe}</p>
            <form>
                <p>{date}</p>
                <input type="date" onChange={(e)=>{setDate(e.target.value)}}/>
                <button>Submit</button>
            </form>
            <button onClick={showSomme()}>Show</button>
        </div>
    );
}

export default Formulaire;