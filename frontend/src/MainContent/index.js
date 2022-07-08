import React from 'react'
import styles from './MainContent.module.css';
import { Routes, Route } from 'react-router-dom';
import Overview from './Overview'
import FoodInfo from './FoodInfo'
import ParkingInfo from './ParkingInfo'
import RoomsInfo from './RoomsInfo'


function index() {
    return (
        <div className={styles["root"]}>
            <Routes>
                <Route path="/" exact element={<Overview />} />
                <Route path="/foodInfo" element={<FoodInfo />} />
                <Route path="/parkingInfo" element={<ParkingInfo />} />
                <Route path="/roomsInfo" element={<RoomsInfo />} />
            </Routes>
        </div>
    )
}

export default index