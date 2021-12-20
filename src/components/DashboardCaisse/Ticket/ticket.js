import React, {useEffect, useState} from 'react';
import './ticket.css';
import {Link,useHistory} from 'react-router-dom'
import Voiture from '../../../models/voiture';
import Reservation from '../../../models/reservation';
import $ from "jquery";
import QRCode from 'qrcode.react';
window.jquery = $;

function Ticket() {
    const history = new useHistory();
    const [voiture, setVoiture]= useState()
    const [reservations , setReservation] = useState(new Reservation())
    const [utilisateur,setUtilisateur] = useState({})
    const [horaireClasse, setHoraireClasse] = useState()
    const [heureDeCreation, setHeureDeCreation] = useState()

    function getDate(){
        var today = new Date();
        var dd = today.getDate();

        var mm = today.getMonth()+1; 
        var yyyy = today.getFullYear();
        var hour = today.getHours();
        var min = today.getMinutes();
    
        if(dd<10) 
        {
            dd='0'+dd;
        } 

        if(mm<10) 
        {
            mm='0'+mm;
        } 
        today = mm+'-'+dd+'-'+yyyy+'  '+hour+':'+min;
        return today
    }

    function setPrenom(prenom){
        let sub = prenom.split(' ');
        return sub[0];
    }

    function getNumberOfPlace(){
        const vip = 10;
        const premium = 16;
        if(horaireClasse.classe.classe === "VIP"){
            return vip
        }else{
            return premium
        }
    }

    function isReserved(value){
        const places = reservations?reservations.position_place.split(','):[];
        let reserved = false;
        (places?places:[]).map((place) => {
            if(place === value){
                //console.log(place + '===' + value)
                reserved = true
             }
        })
        return reserved;
    }

    function impression(){
        let boutton = document.getElementById('boutton');
        boutton.style.visibility = "hidden";
        window.print();
    }

    function annuler(){
        history.push('/homecaisse');
    }

    useEffect(async () => {
        setHeureDeCreation(getDate())
        let voiture_ = await Voiture.get(localStorage.getItem("voiture"))
        //let position = localStorage.getItem("position")
        setVoiture(voiture_)
        let reservation_ = await Reservation.get(localStorage.getItem('reservation'))
        let horaireclasse_ = reservation_.horaireclasse;
        console.log(reservation_);
        setUtilisateur(reservation_.utilisateur);
        setHoraireClasse(horaireclasse_);
        setReservation(reservation_);
        console.log(voiture_);
        console.log(reservation_);
    }, [])

    return (
        <div className='container principal' id='ticket'>
            <div className="container">
                <div className="container" >
                    <div className="mini-container">
                        <p>{heureDeCreation}</p>
                        <p>Société de transport</p>
                        <p>SOATRANS</p>
                    </div>
                    <div className="mini-container">
                        <p><span>NIF: </span>20 042 010 50</p>
                        <p><span>STAT: </span>66303 12 2020 0 01029</p>
                    </div>
                    <div className="container">
                        <div className="p">
                            <p>N°</p>
                            <p>42768512</p>
                        </div>
                        <div className="p">
                            <p>Nom</p>
                            <p>{utilisateur.sexe?<span>Mme.</span>:<span>M.</span>} {utilisateur.last_name?setPrenom(utilisateur.last_name):""}</p>
                        </div>
                        <div className="p">
                            <p>Coordonnée</p>
                            <p>{utilisateur.telephone}</p>
                        </div>
                        <div className="p">
                            <p>Voyage</p>
                            <p>{horaireClasse?horaireClasse.destination.depart:""} - {horaireClasse?horaireClasse.destination.arrive:""}</p>
                        </div>
                        <div className="p">
                            <p>Frais</p>
                            <p>{horaireClasse?horaireClasse.montant_voyage:""} Ar</p>
                        </div>
                        <div className="p">
                            <p>Voiture</p>
                            <p>{voiture?voiture.numero_voiture:""} TBN MR ANDRY</p>
                        </div>
                        <div className="p">
                            <p>Départ</p>
                            <p>{horaireClasse?horaireClasse.destination.depart.toUpperCase():""} {reservations?reservations.date:""} à {horaireClasse?horaireClasse.horaire.heure:""}</p>
                        </div>
                    </div>
                    {(horaireClasse?horaireClasse.classe.classe:"")==="VIP"?
                    (<div className="container">
                        <div className="md-container">
                            <p>{horaireClasse?horaireClasse.classe.classe:""}</p>
                            <div className="row">
                                <div className="row">
                                    <p></p>
                                    <p></p>
                                    {isReserved("1")?<p className="active">1</p>:<p>1</p>}
                                </div>
                                <div className="row">
                                    {isReserved("2")?<p className="active">2</p>:<p>2</p>}
                                    {isReserved("3")?<p className="active">3</p>:<p>3</p>}
                                    {isReserved("4")?<p className="active">4</p>:<p>4</p>}
                                </div>
                                <div className="row">
                                    {isReserved("5")?<p className="active">5</p>:<p>5</p>}
                                    {isReserved("6")?<p className="active">6</p>:<p>6</p>}
                                    {isReserved("7")?<p className="active">7</p>:<p>7</p>}
                                </div>
                                <div className="row">
                                    {isReserved("8")?<p className="active">8</p>:<p>8</p>}
                                    {isReserved("9")?<p className="active">9</p>:<p>9</p>}
                                    {isReserved("10")?<p className="active">10</p>:<p>10</p>}
                                </div>
                            </div>
                        </div>
                        <div className="container">
                            <p>Réservation</p>
                            <div className="container">
                                <p>{horaireClasse?horaireClasse.destination.depart.toUpperCase():""}</p>
                                <p>032 11 906 88</p>
                                <p>{horaireClasse?horaireClasse.destination.arrive.toUpperCase():""}</p>
                                <p>032 11 906 89</p>
                            </div>
                        </div>
                    </div>):
                    (<div className="container flex">
                        <div className="md-container">
                            <div className="container">
                                <div className="row">
                                    <p className='col-1'></p>
                                    <p className='col-1'></p>
                                    {isReserved("1")?<p className='col-1 reserved'>1</p>:<p className='col-1'>1</p>}
                                    {isReserved("2")?<p className='col-1 reserved'>2</p>:<p className='col-1'>2</p>}
                                </div>
                                <div className="row">
                                    {isReserved("3")?<p className='col-1 reserved'>3</p>:<p className='col-1'>3</p>}
                                    {isReserved("4")?<p className='col-1 reserved'>4</p>:<p className='col-1'>4</p>}
                                    {isReserved("5")?<p className='col-1 reserved'>5</p>:<p className='col-1'>5</p>}
                                    {isReserved("6")?<p className='col-1 reserved'>6</p>:<p className='col-1'>6</p>}
                                </div>
                                <div className="row">
                                    {isReserved("7")?<p className='col-1 reserved'>7</p>:<p className='col-1'>7</p>}
                                    {isReserved("8")?<p className='col-1 reserved'>8</p>:<p className='col-1'>8</p>}
                                    <p className='col-1'></p>
                                    {isReserved("9")?<p className='col-1 reserved'>1</p>:<p className='col-1'>9</p>}
                                </div>
                                <div className="row">
                                    {isReserved("10")?<p className='col-1 reserved'>10</p>:<p className='col-1'>10</p>}
                                    {isReserved("11")?<p className='col-1 reserved'>11</p>:<p className='col-1'>11</p>}
                                    <p className='col-1'></p>
                                    {isReserved("12")?<p className='col-1 reserved'>12</p>:<p className='col-1'>12</p>}
                                </div>
                                <div className="row">
                                    {isReserved("13")?<p className='col-1 reserved'>13</p>:<p className='col-1'>13</p>}
                                    {isReserved("14")?<p className='col-1 reserved'>14</p>:<p className='col-1'>14</p>}
                                    {isReserved("15")?<p className='col-1 reserved'>15</p>:<p className='col-1'>15</p>}
                                    {isReserved("16")?<p className='col-1 reserved'>16</p>:<p className='col-1'>16</p>}
                                </div>
                            </div>
                        </div>
                        <div className="container">
                            <p>Réservation</p>
                            <div className="md-container">
                                <p>{horaireClasse?horaireClasse.destination.depart.toUpperCase():""}</p>
                                <p>032 11 906 88</p>
                                <p>{horaireClasse?horaireClasse.destination.arrive.toUpperCase():""}</p>
                                <p>032 11 906 89</p>
                            </div>
                            {horaireClasse?(<QRCode value={reservations.id+"*"+utilisateur.first_name+"*"+horaireClasse.destination.depart+"*"+horaireClasse.destination.arrive}/>):<p></p>}
                        </div>     
                    </div>)}
                    <div className="container" id="boutton">
                        <button type="button" className="btn btn-info" onClick={()=>{impression()}}>Impression</button>
                        <button type="button" className="btn btn-danger" onClick={()=>{annuler()}}>Annuler</button>
                    </div>
                </div>
            </div>
            <iframe name="print_frame" width="0" height="0" frameborder="0" src="about:blank"></iframe>
        </div>
    )
}

export default Ticket;