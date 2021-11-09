import React from 'react'
import { getClassName } from '../../libs/GetCSS'
import cs from './Nodes.module.css'
import star from "./star.png"

const NowNode = ( {node} ) => {

	const handleStarClick = () => {
		
	}

	return (
		<div className={getClassName(["col-8", cs.nowNode])}>
			<div className="card my-2 mx-2">
				<div className="card-body">
					<div className="container row">
						<h6 className="card-title col">
							{node.name}
						</h6>
						<img src={star} alt="star" className={getClassName([cs.star, "col-md-auto"])} onClick={handleStarClick}/>
					</div>
					<div className="card-text">
						{node.desc}
					</div>
				</div>
			</div>
		</div>
	)
}

export default NowNode
