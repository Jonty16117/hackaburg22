import React from 'react'
import styles from './SideNavigation.module.css';
import { Link, useLocation } from "react-router-dom";

function SideNavigation() {
    const location = useLocation();
    console.log(1, location.pathname);
    const getStyle = (currOption) => location.pathname === currOption ? "option-selected" : "option"

    return (
        <div className={styles["root"]}>
            <Link className={styles[getStyle("/")]} to="/" role='button'>Overview</Link>
            <Link className={styles[getStyle("/foodInfo")]} to="/foodInfo" role='button'>Food Info</Link>
            <Link className={styles[getStyle("/parkingInfo")]} to="/parkingInfo" role='button'>Parking Info</Link>
            <Link className={styles[getStyle("/roomsInfo")]} to="/roomsInfo" role='button'>Rooms Info</Link>
        </div>
    )
}

export default SideNavigation