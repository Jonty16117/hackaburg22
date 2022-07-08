import React, { useMemo } from 'react'
import styles from './OverviewChart.module.css'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

function OverviewChart({ labels, data, title }) {
    const chartData = useMemo(() => ({
        labels,
        datasets: [
            {
                label: 'Total people',
                data,
                borderColor: 'rgb(255, 99, 132)',
                backgroundColor: 'rgba(255, 99, 132, 0.5)',
            },
        ],
    }), [labels, data])

    const options = useMemo(() => ({
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: title,
            },
        },
    }), [title])
    return (
        <div className={styles.root}>
            <Line options={options} data={chartData} />
        </div>
    )
}

export default OverviewChart