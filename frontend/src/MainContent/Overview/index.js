import React from 'react'
import OverviewChart from './OverviewChart';
import styles from './Overview.module.css';

const foodLabels = ['Non-Veg', 'Veg', 'Vegan', 'Any'];
const foodData = foodLabels.map(() => Math.floor(Math.random() * 10));

const parkingLabels = ['Spot 1', 'Spot 2', 'Spot 3', 'Spot 4'];
const parkingData = parkingLabels.map(() => Math.floor(Math.random() * 10));

const roomsLabels = ['Room 1', 'Room 2', 'Room 3', 'Room 4'];
const roomsData = roomsLabels.map(() => Math.floor(Math.random() * 10));


function Overview() {
  return (
    <div>
      Overview
      <div className={styles.root}>
        <OverviewChart data={foodData} labels={foodLabels} title={'Food overview'} />
        <OverviewChart data={parkingData} labels={parkingLabels} title={'Parking overview'} />
        <OverviewChart data={roomsData} labels={roomsLabels} title={'Rooms overview'} />
      </div>
    </div>
  )
}

export default Overview