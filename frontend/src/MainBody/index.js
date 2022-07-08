import React from 'react'
import styles from './MainBody.module.css';
import SideNavigation from '../SideNavigation'
import MainContent from '../MainContent'

function index() {
    return (
        <div className={styles["grid-container"]}>
            <SideNavigation />
            <MainContent />
        </div>
    )
}

export default index